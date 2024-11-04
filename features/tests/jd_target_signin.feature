# Created by jyoti at 7/14/2024
Feature: Target sign in feature


  Scenario: User can login to Target sign in page
    Given Open Target sign in page
    When Click Sign In
    And From right side navigation menu, click Sign In
    Then Verify Sign In form opened

    # Enter steps here