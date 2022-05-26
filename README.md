## API tests for course [API Testing in Python](https://testautomationu.applitools.com/python-api-testing/) (Test Automation University)

### Stack
- Python 3.10.2
- pytest 7.1.2 
- Python libraries used: requests, json, jsonpath_ng, lxml, assertpy, Faker, cerberus, pytest-reportportal, pytest-xdist


### Public API used is [people-api](https://github.com/automationhacks/people-api/)

Instruction to set environment is in [README.md](https://github.com/automationhacks/people-api/blob/master/README.md)

### Reports are configured for [Report portal](https://github.com/reportportal/reportportal/blob/master/docker-compose.yml) which is to be deployed via Docker:
```
docker-compose -f docker-compose.yml -p reportportal up -d --force-recreate
```
UI: http://localhost:8080/ui/ (login: superadmin, pass: erebus)
