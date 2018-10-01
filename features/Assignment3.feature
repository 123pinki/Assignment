

Feature: check all functionality
  Scenario: checking keyword identifier, text summarizzation, sentiment analysis, home page, about us section, technology section, solution section, team section and entering the contact detail.

    When Navigate to the stride website
    And Go to the Keyword Identifier
    And Click on load random text
    And Save random text
    And Click on analyze section
    And Enter the text
    And Go to the Text Summarization
    And Enter the text in summarization section
    And Choose compression ratio
    And Go to the Sentiment Analysis
    And Enter the text in sentiment analysis
    And Select the language

    When Go to the HOME page
    And I see the home page

    When Go to the ABOUT US page
    And I see the about page

    When Go to the TECHNOLOGY page
    And I see the technology page

    When Go to the SOLUTION page
    And I see the solution page

    When Go to the TEAM page
    And I see the team page

    When I go to contact page
    And I enter the full name
    And I enter the email id
    And I enter the phone number
    And I enter the text message
    And Save the detail
    And Close the contact section