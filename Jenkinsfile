pipeline {
    agent any
    
    environment {
        SEMGREP = "/usr/local/bin/semgrep-wrapper"
        SCAN_TARGET = "/home/ubuntu/securescan/vulnerable-app"
        RULES_DIR = "/home/ubuntu/securescan/rules"
        REPORT_DIR = "/home/ubuntu/securescan/reports"
    }
    
    triggers {
        githubPush()
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '=== SecureScan SAST Pipeline Starting ==='
                echo "Scanning: ${SCAN_TARGET}"
            }
        }
        
        stage('SAST Scan - Semgrep') {
            steps {
                echo '=== Running Custom Semgrep Rules ==='
                sh '''
                    ${SEMGREP} --config ${RULES_DIR} ${SCAN_TARGET} \
                        --json > ${REPORT_DIR}/jenkins-scan-report.json
                    echo "Scan complete"
                '''
            }
        }
        
        stage('Quality Gate') {
            steps {
                echo '=== Checking Quality Gate ==='
                sh '''
                    ERROR_COUNT=$(${SEMGREP} --config ${RULES_DIR} ${SCAN_TARGET} \
                        --json 2>/dev/null | python3 -c "
import json, sys
data = json.load(sys.stdin)
errors = [r for r in data['results'] if r['extra']['severity'] == 'ERROR']
print(len(errors))
")
                    echo "ERROR findings: ${ERROR_COUNT}"
                    if [ "$ERROR_COUNT" -gt "0" ]; then
                        echo "QUALITY GATE FAILED — ${ERROR_COUNT} ERROR(s) found!"
                        exit 1
                    else
                        echo "QUALITY GATE PASSED"
                    fi
                '''
            }
        }
    }
    
    post {
        failure {
            echo '=== BUILD FAILED — Fix vulnerabilities before merging ==='
        }
        success {
            echo '=== BUILD PASSED — No critical vulnerabilities found ==='
        }
    }
}
