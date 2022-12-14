<h1 align="center"> FlexYoga </h1>

[![Project Status: Active](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)

## Motivation
FlexYoga is a platform that will help users enrol themselves for Yoga classes.
Some of the criteria considered for the same:
* Age Limit: 18-65 years
* Monthly Fee: ₹ 500
* Batches: 4

**Note**: One cannot change batches after enrolling that month. They are allowed to alter batches next month.

## Database Design Schema
Our Database consists of 3 tables
* User Table
    * Stores User details such as Username, age, etc.
* Batch Table
    * Stores details about the batches
* Membership Table
    * Stores Membership details
    * Has a one-one relationship with the User table
      * One user can only hold one membership at a time
      * That membership can only be linked with one user
    * Has a many-one relationship with the Batch table
      * A batch can be linked with multiple memberships
      * Two or more memberships can be linked with the same batch

## ER Diagram
![ER Diagram](https://user-images.githubusercontent.com/70643852/207526925-6d5a8071-e810-4f64-9907-388b4e623bfa.png)

## Process and Steps
* User creates an account. Only users within the range of 18-65 are allowed to do the same
* Once they have logged into their account, they have two options: register or view their user details.
* User details will display when they last registered and their current membership status.
* The web app will give the batch details in the registration form. The user has to select a batch and complete the payment.
* A user who has already enrolled for the month will not be able to enrol again that month. They will have to wait till next month to enrol again (i.e. change batches)
* By enrolling, we mean booking a slot (for that month).
* Every time the user logs in, the application will update the membership status by checking whether the validity of their membership has expired. (This could be an area of improvement)
* User can log out once they are done.

## Points to Note
* We are only allowing a user to enrol once a month. (An alternative could be to let them unenroll that month and then again re-enrol but in the same batch)
* To ensure that only users within the 18-65 age group enrol, we have put an age limit condition while registering.
* Users can securely log in and out of their account using their username and password. This way, one's enrollment is only in their hands.

## Further Improvements / ToDo
- [ ] Automate Script to remove membership from the database, at the end of the month. (Currently doing it using Flask, would like to create a Database Stored Procedure)

## Sample UI Demo

### Details Page
![Detials Page](https://user-images.githubusercontent.com/70643852/207538802-7b2b083b-6381-4d2f-afab-c5a2ab66be6b.png)
### User Enrollment Page
![Enrollment Page](https://user-images.githubusercontent.com/70643852/207539021-6eb3b4de-acde-48a0-93a0-fba8d8949ded.png)


## License 
[![License](https://img.shields.io/badge/License-Apache%202.0-red.svg)](https://opensource.org/licenses/Apache-2.0)
<br/>
This project is under the Apache-2.0 License License. See [LICENSE](LICENSE) for Details.

## Done By
<table>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/70643852?s=96&v=4" width="100px;" height="100px;" alt=""/><br/><sub><b>Pranav B Kashyap</b></sub></a><br/><p align="center">
      <p align="center">
        <a href="https://www.linkedin.com/in/pranav-b-kashyap-1994001b6/" alt="Linkedin">
          <img src="http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width = "30">
        </a>
        <a href="https://github.com/Pranav1007" alt="Github">
          <img src="http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width = "30">
        </a>
      </p>
    </td>
  </tr>
</table>
