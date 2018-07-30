Feature: test

#Scenario for Book


  @slow
  Scenario Outline: Test menu
    Given we on page "page"
    When we click at button "<section>"
    Then I should see the transition to "http://www.wave-access.com/public_en/<sections>.aspx"

    Examples: menu
      | section      | sections     |
      | Services     | services     |
      | Products     | products     |
      | Technologies | technologies |
      | Clients      | clients      |
      | About        | about        |
      | Blog         | blog         |
      | Contact      | contact      |


  Scenario Outline: Test phone call
    Given we on page "page"
    When  we click at button "Technologies"
    And we click at button phone call with id "orderCallLink"
    And we write "<number>" at element with id "TelephoneOrderCall"
    And we write "<name>" at element with id "UsernameOrderCall"
    And we click at cell checkmark
    And we click at button submit
    Then I should see field with id "<id>" and placeholder message "<error>"

    Examples: options
      | number      | name   | error                    | id                 |
      | 123         | aaaa   | Phone field is mandatory | TelephoneOrderCall |
      |             | Julian | Phone field is mandatory | TelephoneOrderCall |
      | 79347643603 |        | Name field is mandatory  | UsernameOrderCall  |


  Scenario Outline: Test links
    Given we on page "page"
    When we click at button "Products"
    And in section "<products>" we click at button details
    Then I should see the transition to "<links>"

    Examples: links
      | products                                      | links                                                                               |
      | myQuiz                                        | http://myquizhub.com                                                                |
      | Event Game                                    | http://www.eventquizgames.com                                                       |
      | CRM Gamification Tool                         | http://www.wave-access.com/public_en/ms_crm_gamification_product.aspx               |
      | Relationship Charts                           | http://www.wave-access.com/public_en/relationship_charts.aspx                       |
      | Asterisk & Elastix & Dynamics CRM Integration | http://www.wave-access.com/public_en/asterisk-elastix-dynamics-crm-integration.aspx |
      | Singlepoint                                   | http://www.single-point.ru                                                          |
      | OnlineShop                                    | http://www.wave-access.com/public_en/online_shop.aspx                               |
      | ChatOnline                                    | http://www.wave-access.com/public_en/chat_online.aspx                               |
      | OnlineHelp                                    | http://www.wave-access.com/public_en/online_help.aspx                               |
      | eService & ChatOnline CRM Accelerator         | http://www.wave-access.com/public_en/portal.aspx                                    |

  Scenario Outline: Negative test form filling
    Given we on page "page"
    When  we click at button Get started
    And we write "<email>" at element with id "getStartedEmail"
    And we write "<name>" at element with id "getStartedUsername"
    And we click at cell checkmark
    And we click at button submit
    Then I should see field with id "<id>" and placeholder message "<error>"

    Examples:
      | email                | name   | error                             | id                 |
      | 123                  | Julian | Sorry, we did not catch your mail | getStartedEmail    |
      |                      | Julian | Email field is mandatory          | getStartedEmail    |
      | oxana-popova@mail.ru |        | Name field is mandatory           | getStartedUsername |


  Scenario Outline: Positive test form filling
    Given we on page "page"
    When  we click at button Get started
    And we write "<email>" at element with id "getStartedEmail"
    And we write "<name>" at element with id "getStartedUsername"
    And we click at cell checkmark
    And we click at button submit
    Then I should see message "<success>" at element with id "<id>"

    Examples:
      | email                | name   | success                                                                | id                |
      | oxana-popova@mail.ru | Oksana | We have received your enquiry and will respond to you within 24 hours. | successGetStarted |
