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
 				// This step should not normally be used in your script. Consult the inline help for details.
					dockerFingerprintRun 'cda73647254a'
 			}
 		}
// 		stage("run") {
//  			steps {
//  				sh "docker run --rm test"
//  			}
//  		}
         
 	}
}
