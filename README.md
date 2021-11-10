### home_task

# Introduction 

Python code which will print the number from 1 to 10 in random order

<!--- BEGIN_TF_DOCS --->

## Requirements

| Name | Version |
|------|---------|
| python | 3.8 |

## Prerequisite

Install python on your Linux or Mac machines (workstation) by folllowing below instructions.

### Install Python 3 on Linux

```
### Implementation

$ sudo apt update  				                #Update and Refresh Repository Lists
$ sudo apt install software-properties-common	#Install Supporting Software
$ sudo add-apt-repository ppa:deadsnakes/ppa	#Add Deadsnakes PPA
$ sudo apt install python3.8 		        	#Install Python 3
$ python --version				                #Check installed python version

```
### Installing Python 3 on Mac OS X

Before installing Python, you’ll need to install GCC. GCC can be obtained by downloading Xcode, the smaller Command Line Tools (must have an Apple account) or the even smaller OSX-GCC-Installer package.

```
### Implementation
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"     # Install Homebrew
$ export PATH="/usr/local/opt/python/libexec/bin:$PATH"                                                 # Set PATH Environment
$ $ brew install python                                                                                 # Install python 3
$ python3  --version                                                                                    # To check python version
```

For more information please follow refrence links:
* [Install python on Linux](https://phoenixnap.com/kb/how-to-install-python-3-ubuntu)
* [Install python on Mac](https://realpython.com/installing-python/#how-to-install-python-on-macos)


## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| bucketName | S3 buckets need to be created | `string` | `null` | yes |


## Implementation

## Task
- Create terraform S3 bucket module with lifecycle rule

```
## Outputs

$ git clone https://github.com/manukoli1986/zenjob_devops_task.git
$ cd terraform-s3/
$ terraform init
$ terraform apply --var-file=qa.tfvars 
OR 
$ terraform apply --var-file=staging.tfvars
```



## 2nd Task
- Develop and deploy a dockerize python app that will write a new file to S3 in every 5 minutes of interval. These files need to be maintained only for 24h
- The file should be date and time format i.e. 2021-11-07 18:02:59.670622-data.txt
- Will use AWS_DEFAULT_REGION, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as environment variables which will be used by python boto client to access S3 service
- My python code is consuming envrionment variable to access the aws credentials
- In kubernetes, we need to create secret objects as environment variabls to store keys (secret.yaml)
- Using kubernetes cronjob to run python as on kubenetes cluster in every 5 minutes

```
## Outputs

$ git clone https://github.com/manukoli1986/zenjob_devops_task.git
$ cd code/

Build and upload the docker image according to your requirement. Currently I am using dockerhub public for python app.
$ docker build -t manukoli1986/create-object-s3:v1 .
$ docker push manukoli1986/create-object-s3:v1

To Test the docker image running as expected please use below command or you can skip it. 
$ docker run --env AWS_DEFAULT_REGION="XXX" --env AWS_ACCESS_KEY_ID="XXX" --env AWS_SECRET_ACCESS_KEY="XXX"  manukoli1986/create-object-s3:v1 staging-mayank-koli-platform-challenge

Now let's generate AWS_DEFAULT_REGION, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as environment variables by replacing them with their values in below command and update in secret.yaml
$ cd k8s/
$ echo -n "AWS_DEFAULT_REGION" | base64
$ echo -n "AWS_ACCESS_KEY_ID" | base64
$ echo -n "AWS_SECRET_ACCESS_KEY" | base64

Let's deploy kubernetes cronjob object in different namespaces
QA NS
$ kubectl create ns qa
$ kubectl create -f secret.yaml -n qa
$ kubectl create -f cronjob-qa.yaml 

STAGING NS
$ kubectl create ns staging
$ kubectl create -f secret.yaml -n staging
$ kubectl create -f cronjob-staging.yaml 

```

## Best Practices Can Be Implemented

Due to time constraints of 2 hours, I could simply write the code and deploy it as expected. But we should definatley follow the best practice.
- Recommended way is to use aws role on kubernetes with the help of KIAM (https://github.com/uswitch/kiam) 
OR
- Attaching an IAM policy to the node(s) role - Disadvantage - The downside of this approach is that it grants those permissions to all pods running on that node
OR
- Assigning an IAM role to a service account- This allows you to isolate permissions of different pods. This option is a little more complicated since it involves creating an OIDC identity provider on your cluster.
OR
- (AWS Fargate only) Pod execution roles- If you are using AWS Fargate to run your pods, then you should be able to add permissions to your pod execution role.
- Even we can create helm chart of this code which will be more easy to deploy the code with environment specific. 
- If we go with IAM ROLE or POLICY way then make sure they are in AWS_DEFAULT_REGION, AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY as environment variables order. This will require little changes in kubernetes resource file i.e add serviceAccount.


## Author

Mayank Koli
