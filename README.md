# SecureScan — Custom SAST Rules Engine

A DevSecOps project demonstrating custom Semgrep rules and Jenkins CI/CD pipeline with security quality gates.

## Project Structure
## Vulnerabilities Detected
| Rule | Vulnerability | OWASP | Severity |
|------|--------------|-------|----------|
| python-sqli-string-concat | SQL Injection via string concat | A03 | ERROR |
| python-sqli-fstring | SQL Injection via f-string | A03 | ERROR |
| python-sqli-format | SQL Injection via .format() | A03 | ERROR |
| python-os-system-injection | Command Injection via os.system() | A03 | ERROR |
| python-subprocess-shell-true | Command Injection via subprocess | A03 | ERROR |
| python-os-popen-injection | Command Injection via os.popen() | A03 | ERROR |
| python-eval-injection | Eval Injection | A03 | ERROR |
| python-exec-injection | Code Injection via exec() | A03 | ERROR |
| hardcoded-aws-access-key | AWS Key Hardcoded | A02 | ERROR |
| hardcoded-db-password | DB Password Hardcoded | A02 | ERROR |
| hardcoded-secret-key | Secret Key Hardcoded | A02 | ERROR |
| python-path-traversal-open | Path Traversal via open() | A01 | ERROR |
| python-path-traversal-with-open | Path Traversal via with open() | A01 | ERROR |
| python-weak-hash-md5 | Weak Crypto — MD5 | A02 | ERROR |
| python-weak-hash-sha1 | Weak Crypto — SHA1 | A02 | WARNING |

## Jenkins Pipeline
- **Stage 1:** Checkout
- **Stage 2:** SAST Scan — Semgrep with 15 custom rules
- **Stage 3:** Quality Gate — Build FAILS if ERROR count > 0

## Results
- Rules: 15 custom rules across 6 vulnerability categories
- Findings: 8/8 vulnerabilities detected
- Quality Gate: FAILED (as expected — vulnerable app)

## Tech Stack
- Semgrep 1.161.0
- Python 3.12 / Flask
- Jenkins 2.541
- Ubuntu 24.04 / AWS EC2
# Webhook test
