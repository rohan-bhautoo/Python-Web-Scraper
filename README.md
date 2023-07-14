<p align="center">
  <img src="https://i.ibb.co/NrXZhT8/Web-Scraping.png">
</p>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-brightgreen.svg" />
  <img alt="PHP" src="https://img.shields.io/badge/PHP-777BB4?logo=php&logoColor=white" />
  <img alt="Symfony" src="https://img.shields.io/badge/Symfony-000000?logo=symfony&logoColor=white" />
  <img alt="Composer" src="https://img.shields.io/badge/Composer-7A6E7E?logo=composer&logoColor=white" />
  <img alt="Docker" src="https://img.shields.io/badge/Docker-0db7ed?logo=docker&logoColor=white" />
  <img alt="Tailwind CSS" src="https://img.shields.io/badge/Tailwind CSS-3490DC?logo=tailwindcss&logoColor=white" />
</p>

This guide will help you to learn PHP Symfony 6 Framework basics. The concepts in this course include:
* Basic of handling requests
* Twig templates
* Databases and Doctrine
* Doctrine Relations
* Querying the database
* Authentication (registration, e-mail confirmation, login page, banning users)
* Authorization of users (roles, voters)
* User permission system (role-based)
* File uploads and displaying uploaded images
* Sending e-mail

You'll learn all this while building a fun and interesting project, a Twitter-like clone, using the most modern CSS framework Tailwind CSS.

<p align="center">
  <img src="https://i.ibb.co/k3k9JXP/How-Symfony-Works-2x.png">
</p>

## Get Started

### Setup / Installation

#### PHP 8.1
PHP will be used  to run a built-in server and run console commands. Install PHP 8.1 or higher. Download the Thread safe version [here](https://windows.php.net/download#php-8.1).

<details><summary><b>Show Steps</b></summary>

1. Extract the downloaded zip file in ```C:\Program Files\``` directory.

2. Copy the full directory of the extracted folder.

3. Now click on Start Menu and search ```Environment variables``` and open it.

4. Under System variables, add a new value inside the ```Path``` variable and paste the full directory in step 2.

5. Save your changes and check the php version in command prompt.

    ```shell
    php --version
    PHP 8.1.13 (cli) (built: Nov 22 2022 15:49:14) (ZTS Visual C++ 2019 x64)
    Copyright (c) The PHP Group
    Zend Engine v4.1.13, Copyright (c) Zend Technologies
    ```

</details>

#### Composer
Composer will be used to install PHP packages. Download it [here](https://getcomposer.org/download/).

<details><summary><b>Show Installations</b></summary>

1. Windows Installer - The installer, which requires that you have PHP already installed, will download Composer for you and set up your PATH environment variable so you can simply call composer from any directory. Download and run [Composer-Setup.exe](https://getcomposer.org/Composer-Setup.exe) - it will install the latest composer version whenever it is executed.

2. Command-line installation - To quickly install Composer in the current directory, run the following script in your terminal. Use this [guide to install Composer programatically](https://getcomposer.org/doc/faqs/how-to-install-composer-programmatically.md).

    ```sh
    php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
    php -r "if (hash_file('sha384', 'composer-setup.php') === '55ce33d7678c5a611085589f1f3ddf8b3c52d662cd01d4ba75c0ee0459970c2200a51f492d557530c71c15d8dba01eae') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
    php composer-setup.php
    php -r "unlink('composer-setup.php');"
    ```

</details>

#### Symfony CLI
Download the 386 binaries [here](https://symfony.com/download).

<details><summary><b>Show Installations</b></summary>
  
  1. Extract the ZIP file to C:\symfony-cli.
  
  2. Add to the Path environment variable under ***User Variables***.
  
  3. Run ```symfony``` in terminal to see the CLI version and commands.
  
  <p align="center">
    <img width="600" height="400" src="https://user-images.githubusercontent.com/47154593/212466111-18f4d35e-87b7-47ea-a3cd-04be8493f3f5.png">
  </p>

</details>

#### Docker
Docker will be used to run a database server and db admin panel.

## Symfony 101

### Creating Project
Open your console terminal and run any of these commands to create a new Symfony application:

#### Symfony-cli
```shell
symfony new my_project_directory --version="6.2.*"
```



## Author

👤 **Rohan Bhautoo**

* Github: [@rohan-bhautoo](https://github.com/rohan-bhautoo)
* LinkedIn: [@rohan-bhautoo](https://linkedin.com/in/rohan-bhautoo)

## Show your support

Give a ⭐️ if this project helped you!
