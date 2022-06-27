# Scott Sucks At Programming's Clean Smart Contract Check List

## ReneeCoins.sol

- [x] <span style="color:green">Naming</span>

  - [x] File / module / contract names reveal their intention, context and
        use cases.
  - [x] Function names reveal their intention, context and use cases.
  - [x] Variable names reveal their intention, context and use cases.
  - [x] Names are human readable and pronounceable.
  - [x] Names are searchable.
  - [x] Names are consistent.

- [x] <span style="color:green">Structure and Ordering</span>

  - [x] Does my code follow the standard structure.
  - [x] Are the functions modifiers in the correct order?
  - [x] Is the visibility of functions explicitly documented?
  - [x] Is the visibility of state variables explicitly documented?

- [x] <span style="color:green">Comments and Documentation</span>

  - [x] Are my comments written in the correct format?
  - [x] Are the comments explicit and provide additional details to the end-users or other developers?
  - [x] Are the comments up to date?

- [x] <span style="color:green">Formatting</span>

  - [x] Is my code formatted consistently?
  - [x] Am I following the style guide?
  - [x] Has my linter formatted my code?

- [x] <span style="color:green">Contract and Data Structures</span>

  - [x] Are my data structures designed intuitively?
  - [x] Are my data structures named well and easily found?
  - [x] Is there data that can be moved off chain, to another part of the contract, or to a better place?

- [x] <span style="color:green">Systems</span>

  - [x] Is there a simpler way to design this contract / Module/
  - [x] Does this module / contract have only one responsibility?
  - [x] Do my functions have only one responsibility? Can they be split?
  - [x] Consider any functions that are longer than 5 lines of code to be
        split into multiple functions.

- [x] <span style="color:green">Standards and Libraries</span>

  - [x] Does my contract import acceptable standards?
  - [x] Are there any standards I can add to replace custom code?

- [x] <span style="color:green">Error Handling</span>

  - [x] Are my error messages explicit? Do they explain the source and cause
        of the error?
  - [x] Do I have tests which cover all errors?
  - [x] Are there places where [[Guard Check]]s would have prevent issues or
        be effective at ensuring contract behavior is as expected?

- [x] <span style="color:green">Testing</span>
  - [x] Do I have tests proving the behavior of my code functions as
        expected?
  - [x] Do my tests have only a single assert?
  - [x] Have I followed the FIRST and AAA patterns for testing?

## ReneeLaneCollection.sol

- [ ] <span style="color:red">Naming</span>

  - [ ] File / module / contract names reveal their intention, context and
        use cases.
  - [ ] Function names reveal their intention, context and use cases.
  - [ ] Variable names reveal their intention, context and use cases.
  - [ ] Names are human readable and pronounceable.
  - [ ] Names are searchable.
  - [ ] Names are consistent.

- [ ] <span style="color:red">Structure and Ordering</span>

  - [ ] Does my code follow the standard structure.
  - [ ] Are the functions modifiers in the correct order?
  - [ ] Is the visibility of functions explicitly documented?
  - [ ] Is the visibility of state variables explicitly documented?

- [ ] <span style="color:red">Comments and Documentation</span>

  - [ ] Are my comments written in the correct format?
  - [ ] Are the comments explicit and provide additional details to the end-users or other developers?
  - [ ] Are the comments up to date?

- [ ] <span style="color:red">Formatting</span>

  - [ ] Is my code formatted consistently?
  - [ ] Am I following the style guide?
  - [ ] Has my linter formatted my code?

- [ ] <span style="color:red">Contract and Data Structures</span>

  - [ ] Are my data structures designed intuitively?
  - [ ] Are my data structures named well and easily found?
  - [ ] Is there data that can be moved off chain, to another part of the contract, or to a better place?

- [ ] <span style="color:red">Systems</span>

  - [ ] Is there a simpler way to design this contract / Module/
  - [ ] Does this module / contract have only one responsibility?
  - [ ] Do my functions have only one responsibility? Can they be split?
  - [ ] Consider any functions that are longer than 5 lines of code to be
        split into multiple functions.

- [ ] <span style="color:red">Standards and Libraries</span>

  - [ ] Does my contract import acceptable standards?
  - [ ] Are there any standards I can add to replace custom code?

- [ ] <span style="color:red">Error Handling</span>

  - [ ] Are my error messages explicit? Do they explain the source and cause
        of the error?
  - [ ] Do I have tests which cover all errors?
  - [ ] Are there places where [[Guard Check]]s would have prevent issues or
        be effective at ensuring contract behavior is as expected?

- [ ] <span style="color:red">Testing</span>
  - [ ] Do I have tests proving the behavior of my code functions as
        expected?
  - [ ] Do my tests have only a single assert?
  - [ ] Have I followed the FIRST and AAA patterns for testing?
