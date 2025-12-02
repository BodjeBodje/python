1. Install Pip
sudo apt install python3 python3-pip

2. Install Venv: a utility for creating python virtual env
sudo apt install python3-venv

3.Create a virtual ENV:class24
 python3 -m venv class24

4. Activate the Virtual Env
source class24/bin/activate

The env name should appear before the pc name in terminal(activate)


5. Install cli
sudo snap install aws-cli --classic
OR
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip -q awscliv2.zip
sudo ./aws/install

aws --version
aws configure
               Go aws account->IAM -> user ->access key
               (aws_access_key_id:YOUR_KEY
               aws_secret_access_key:YOUR_SECRET)
aws s3 ls

6. Install Dependencies
Boto3: This is a library  for interacting with aws
    https://pypi.org/project/boto3/
python -m pip install boto3

7. aws amd boto3
https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html