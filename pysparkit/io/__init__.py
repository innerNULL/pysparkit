# -*- coding: utf-8 -*-
# file: __init__.py
# date: 2021-07-20


import os
import _io
import json
import logging
import time
import datetime
import pyspark
import pyspark.sql
from typing import Any, Union, Dict, List, Tuple

from ... import pysparkit


LOGGER: logging.Logger = pysparkit.get_logger(__name__, level=logging.INFO)


def json_file2dict(json_path: str) -> Dict:
    """ Loads a json file as python `Dict` instance. """
    output: Dict
    json_file: _io.TextIOWrapper = open(json_path)
    output = json.load(json_file)
    json_file.close()
    return output


def get_fs_proto(path: str) -> str:
    """Get file-system's type/proto from path string.

    Args:
        path: The path(directory or file path) waiting to judge.

    Returns:
       The file-system proto type, "file" represents local file-
       system.
    """
    decompose: Tuple = path.split(":")
    if len(decompose) < 2 or decompose[0] == "file":
        return "file"
    else:
        return decompose[0]


def if_fs_client_ok(fs_client: str) -> bool:
    """If file-system executable file ok for using with command line.

    Args:
        fs_client: Ref to `py_dict_rdd2disk`.
    """
    client_path: str = os.popen("which %s" % fs_client).read().strip("\n")
    return len(client_path) > 2


def hadoop_reset_directory(
        directory: str, backup_postfix: str="_bak") -> None:
    """Resets an (existing) directory which using hadoop as client.

    Mainly includes following process:
        1. Remove historical backup directory.
        2. Backup `directory` if it already exist.
        3. Remove `directory`, but it should actually not exists after
           backup process.
        4. Build `directory`'s parent directory in case it not actually 
           exists.

    Args:
        directory: The directory waiting to reset with hadoop client.
        backup_postfix: Ref to `py_dict_rdd2disk`.
    """
    backup_dir: str = directory + backup_postfix
    
    clean_bak_cmd: str = "hadoop fs -rm -r %s" % backup_dir
    backup_cmd: str = "hadoop fs -mv %s %s" % (directory, backup_dir)
    clean_cmd: str = "hadoop fs -rm -r %s" % directory
    build_cmd: str = "hadoop fs -mkdir -p %s" % os.path.dirname(directory)

    LOGGER.info(os.popen(clean_bak_cmd).read())
    LOGGER.info(os.popen(backup_cmd).read())
    LOGGER.info(os.popen(clean_cmd).read())
    LOGGER.info(os.popen(build_cmd).read())


def before_data2disk(target_directory: str, 
        fs_client: str="default", backup_postfix: str="_bak") -> None:
    """Preprocessing before `RDD` data persistence.

    Mainly include get the file-system type/proto, do some directory 
    backup/building job.

    Args:
        target_directory: Ref to `py_dict_rdd2disk`.
        fs_client: Ref to `py_dict_rdd2disk`.
        backup_postfix: Ref to `py_dict_rdd2disk`.
    """
    if get_fs_proto(target_directory) != "file" and fs_client == "default":
        fs_client = "hadoop"

    if not if_fs_client_ok(fs_client):
        raise Exception("Your %s client is not OK, check it." % fs_client)

    if fs_client == "hadoop":
        hadoop_reset_directory(target_directory, backup_postfix)
    else:
        # TODO@202107211350
        raise Exception("For now only support hadoop fs client.")


def py_dict_rdd2disk(py_dict_rdd: pyspark.RDD, 
        target_directory: str, fs_client: str="default", 
        backup_postfix: str="_bak") -> None:
    """python `Dict` rdd persistence function.

    Persistence a python `Dict` spark rdd to file-system, which could 
    be local file-system or hdfs style distributed fs.

    Args: 
        py_dict_rdd: 
            Spark `RDD` waiting to persistence, each record should be 
            a python `Dict` instance.
        target_directory: 
            The directory path to which we hope persistence `py_dict_rdd`. 
        fs_client: 
            The file-system interaction client, not necessary for local-
            file-system, but necessary for remote or distributed file-
            system, for example, hadoop for hdfs. And `fs_client` is 
            the name of certain file-system executable file name.
        backup_postfix:
            If the `target_directory` already exists, we will backup it 
            first under the same parent directory, with appending 
            `backup_postfix` as the postfix of backup directory.
    """
    before_data2disk(target_directory, fs_client, backup_postfix)

    json_rdd: pyspark.RDD = py_dict_rdd\
            .map(lambda x: json.dumps(x, separators=(',', ':')))\
            .saveAsTextFile(target_directory)


def hadoop_if_path_exists(path: str) -> bool:
    if not if_fs_client_ok("hadoop"):
        raise Exception("hadoop client is not OK")

    hadoop_cmd: str = "hadoop fs -ls %s" % path
    cmd_result: str = os.popen(hadoop_cmd).read()
    
    if "No such file or directory" in cmd_result:
        return False
    return True


def hadoop_waiting_util_path_ready(
        path: str, waiting_seconds: int=1, 
        logging_period: int=30
) -> None:
    start_time: datetime.datetime = datetime.datetime.now() 
    while True:
        if hadoop_if_path_exists(path):
            LOGGER.info("path '%s' has been ready." % path)
            break
        else:
            now: datetime.datetime = datetime.datetime.now()
            waiting_seconds_: datetime.timedelta = (now - start_time).seconds
            if waiting_seconds_ > waiting_seconds:
                LOGGER.info("Out of waiting time for path '%s'..." % path)
                break
            else:
                if waiting_seconds_ % logging_period == 0:
                    LOGGER.info("Waiting for path '%s' ready..." % path)


def json_line_files2py_dict_rdd(
        sc: pyspark.sql.SparkSession, path: str
) -> pyspark.RDD:
    return sc.sparkContext.textFile(path)\
            .map(lambda x: json.loads(x))

