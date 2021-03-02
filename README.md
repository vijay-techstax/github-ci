# Github Integration Example Project

This is a sample repo to demonstrate a working of Github's Continuous Integation and Deployment using Github actions.

****************************

## Branches

* `prod` -> Production Branch (Stable Releases - After passing all unit tests + integration tests)
* `staging` -> Staging Branch (Fairly Stable release - After passing all unit tests + integration tests)
* `dev` -> Development Branch (Unstable Branch)

## Workflow

1. Push to `dev` branch locally
2. Run all test cases
3. Stable version gets merged with `staging`
4. Run all unit tests + integration tests
5. Stable version gets merged with `prod`

*****************************