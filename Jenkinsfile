pipeline {
	agent any
	//agent { docker { image 'python:3.7.2' } }
 	stages {
 		stage("Compile") {
 			steps {
 				echo "no need to build python code"
 			}
 		}
 		stage("Unit test") {
 			steps {
 				sh "python test_sum_num.py"
 			}
 		}
		stage("build") {
 			steps {
 				sh """docker build -t test ."""
 			}
 		}
// 		stage("run") {
//  			steps {
//  				sh "docker run --rm test"
//  			}
//  		}
         
 	}
}
