Feature: behave demo for Mahara login

Scenario: valid user can login Mahara site
    Given a valid user name and password
     When a valid user clicking on the login button after typing in user name and password
     Then logout link should display
