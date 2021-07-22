# pysparkit (PYSPARK kIT)
For now this lib is still in development, it's just a collection of wrapper-utils from my recent years' pyspark development experimence. These simple but useful wrapped-utils functions can make pyspark application deveploment be more easily.

## Features
* **Self Contained**: pysparkit it self dosn't needs any outer dependencies, so it's easy to distribute cross yarn computation nodes by spark-submit's `--py-files` parameter. But some sub-module under incubator may needs outer dependencies.

# files organization
## pysparkit/lambda\_ops
Here will put some basic lambda data-handling operators, I group the lambda operators to three part: Map, Reduce and Filter.
### pysparkit/lambda\_ops/map\_ops
### pysparkit/lambda\_ops/reduce\_ops
Spark provides many reduce-style interfaces, such as `reduce`, `reduceByKey`, `combineByKey`, `aggregateByKey`, `foldByKey` etc.

