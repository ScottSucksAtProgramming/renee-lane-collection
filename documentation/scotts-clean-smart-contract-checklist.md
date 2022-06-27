# Scott Sucks At Programming's Clean Smart Contract Check List

## ReneeCoins.sol

- [x] Naming

  - [x] File / module / contract names reveal their intention, context and
        use cases.
  - [x] Function names reveal their intention, context and use cases.
  - [x] Variable names reveal their intention, context and use cases.
  - [x] Names are human readable and pronounceable.
  - [x] Names are searchable.
  - [x] Names are consistent.

- [x] Structure and Ordering

  - [x] Does my code follow the standard structure.
  - [x] Are the functions modifiers in the correct order?
  - [x] Is the visibility of functions explicitly documented?
  - [x] Is the visibility of state variables explicitly documented?

- [x] Comments and Documentation

  - [x] Are my comments written in the correct format?
  - [x] Are the comments explicit and provide additional details to the end-users or other developers?
  - [x] Are the comments up to date?

- [x] Formatting

  - [x] Is my code formatted consistently?
  - [x] Am I following the style guide?
  - [x] Has my linter formatted my code?

- [x] Contract and Data Structures

  - [x] Are my data structures designed intuitively?
  - [x] Are my data structures named well and easily found?
  - [x] Is there data that can be moved off chain, to another part of the contract, or to a better place?

- [x] Systems

  - [x] Is there a simpler way to design this contract / Module/
  - [x] Does this module / contract have only one responsibility?
  - [x] Do my functions have only one responsibility? Can they be split?
  - [x] Consider any functions that are longer than 5 lines of code to be
        split into multiple functions.

- [x] Standards and Libraries

  - [x] Does my contract import acceptable standards?
  - [x] Are there any standards I can add to replace custom code?

- [x] Error Handling

  - [x] Are my error messages explicit? Do they explain the source and cause
        of the error?
  - [x] Do I have tests which cover all errors?
  - [x] Are there places where [[Guard Check]]s would have prevent issues or
        be effective at ensuring contract behavior is as expected?

- [x] Testing
  - [x] Do I have tests proving the behavior of my code functions as
        expected?
  - [x] Do my tests have only a single assert?
  - [x] Have I followed the FIRST and AAA patterns for testing?

## ReneeLaneCollection.sol

- [ ] Naming

  - [ ] File / module / contract names reveal their intention, context and
        use cases.
  - [ ] Function names reveal their intention, context and use cases.
  - [ ] Variable names reveal their intention, context and use cases.
  - [ ] Names are human readable and pronounceable.
  - [ ] Names are searchable.
  - [ ] Names are consistent.

- [ ] Structure and Ordering

  - [ ] Does my code follow the standard structure.
  - [ ] Are the functions modifiers in the correct order?
  - [ ] Is the visibility of functions explicitly documented?
  - [ ] Is the visibility of state variables explicitly documented?

- [ ] Comments and Documentation

  - [ ] Are my comments written in the correct format?
  - [ ] Are the comments explicit and provide additional details to the end-users or other developers?
  - [ ] Are the comments up to date?

- [ ] Formatting

  - [ ] Is my code formatted consistently?
  - [ ] Am I following the style guide?
  - [ ] Has my linter formatted my code?

- [ ] Contract and Data Structures

  - [ ] Are my data structures designed intuitively?
  - [ ] Are my data structures named well and easily found?
  - [ ] Is there data that can be moved off chain, to another part of the contract, or to a better place?

- [ ] Systems

  - [ ] Is there a simpler way to design this contract / Module/
  - [ ] Does this module / contract have only one responsibility?
  - [ ] Do my functions have only one responsibility? Can they be split?
  - [ ] Consider any functions that are longer than 5 lines of code to be
        split into multiple functions.

- [ ] Standards and Libraries

  - [ ] Does my contract import acceptable standards?
  - [ ] Are there any standards I can add to replace custom code?

- [ ] Error Handling

  - [ ] Are my error messages explicit? Do they explain the source and cause
        of the error?
  - [ ] Do I have tests which cover all errors?
  - [ ] Are there places where [[Guard Check]]s would have prevent issues or
        be effective at ensuring contract behavior is as expected?

- [ ] Testing
  - [ ] Do I have tests proving the behavior of my code functions as
        expected?
  - [ ] Do my tests have only a single assert?
  - [ ] Have I followed the FIRST and AAA patterns for testing?
