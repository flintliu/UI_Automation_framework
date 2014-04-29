ATF 
==============
Abaisse Testing Framework

Abaisse Testing Framework is a tool set and structure to help tester design and write UI, interface and backend test suite. Strictly speaking, it is not a framework, more likes a automation concept or method.

Generally for a test suite, there are three layers which are "test case", "action" and "driver". 
###“test case”
business process
###"action"
singel action such as login
###"driver"
    interfaces: get, post, put, delete
    |
    UI page module
        |
        page module driver
        |
        object module
    |
    log driver
        |
        relationship parser
        |
        log parser
    |
    mock service
        |
        web service
