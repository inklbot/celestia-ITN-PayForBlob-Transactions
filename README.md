This Github repository has already been submitted to Celestia ITN Bonus Tasks
<br/>
So copying and submitting assignments is not a good idea and should only be used for inspiration
<br/>

# Overview
#### This guide provides two methods for running PayForBlob Transactions.<br/><br/>
[Method_1 - CLI](https://github.com/inklbot/celestia-ITN-PayForBlob-Transactions/blob/main/README.md#method_1-guide)<br/>
The CLI version helps you create `PayForBlob Tx` with a simple one-line command on the server running celestia-node
<br/>

[Method_2 - UI](https://github.com/inklbot/celestia-ITN-PayForBlob-Transactions/blob/main/README.md#method_2-guide)<br/>
The GUI version uses Python to connect to ssh and run PayForBlob Tx with a simple button
<br/>

[Method_3 - GUI](https://github.com/inklbot/celestia-ITN-PayForBlob-Transactions/blob/main/README.md#method_3-guidewindows-10)<br/>
The GUI version helps you create `PayForBlob Tx` from anywhere after a simple setup on the server running celestia-node
<br/>

[Phase_3 Guide](https://github.com/inklbot/celestia-ITN-PayForBlob-Transactions/blob/main/README.md#phase-3-guide)<br/>
<br/>

## Method_1 guide

#### Enter this command on the server running Celestia-node.
```
wget https://raw.githubusercontent.com/inklbot/celestia-itn/main/blob.sh && sed -i 's/\r//' blob.sh && chmod +x blob.sh && sudo /bin/bash blob.sh
```

## Method_1 Example
#### Run `blob.sh`
<img width="80%" src="https://user-images.githubusercontent.com/31788091/229029309-50a1ebe6-e55f-48b1-bd72-9a78e5e17105.PNG"/>
<br/>
<img width="80%" src="https://user-images.githubusercontent.com/31788091/229029310-a5a5c3fd-b1a5-4929-9fe3-b54222ece5ed.PNG"/>
<br/>
<img width="80%" src="https://user-images.githubusercontent.com/31788091/229029313-0e3e49d5-fdf1-4785-8f57-e1d0e5b20a7f.PNG"/>
<br/> When you ran the `blob.sh`
<br/><br/>
<img width="80%" src="https://user-images.githubusercontent.com/31788091/229029315-89ebb6d7-80ac-476e-a80a-90ab3454d562.PNG"/>
<br/>Go through the attached mintscan link and check if the TxHash, Height, and Wallet address are correct
<br/>
<br/><br/>
<img width="80%" src="https://user-images.githubusercontent.com/31788091/229029324-ac465602-c946-4425-9678-b712f963ccb4.PNG"/>
<br/>Go to tiascan and check the PayForBlob Count.

## Method_2 guide

Install `screen, python3, pip` and install `flask` module
<br/>

```
sudo apt install screen python3 python3-pip -y
pip install flask
```
<br/>

Download `web_server.py`

<br/>

```
wget https://raw.githubusercontent.com/inklbot/celestia-ITN-PayForBlob-Transactions/main/web_server.py https://raw.githubusercontent.com/inklbot/celestia-itn/main/blob.sh
```

<br/>

Create `dashboard` folder and download index.html

<br/>

```
mkdir dashboard
cd dashboard
wget https://raw.githubusercontent.com/inklbot/celestia-ITN-PayForBlob-Transactions/main/index.html
cd ..
```

<br/>
Split terminal using screen
<br/>

```
screen -S web_server
```

<br/>

Run `web_server.py` in a split terminal

<br/>

```
python3 web_server.py
```
![image](https://user-images.githubusercontent.com/31788091/229338507-c71176c3-a864-466c-bc35-feaa0a216aab.png)
<br/>
Now you're all set.<br/>
Then type `CTRL+A+D` simultaneously to return to the original terminal.

<br/>


## Method_2 Example
<br/>

Access the dashboard via the website at `http://<server-ip>:5000/`

<br/>

![image](https://user-images.githubusercontent.com/31788091/229338614-590201da-ef78-498e-ac02-be02db80479a.png)

`Execution` button executes PayForBlob transactions.
<br/>

![image](https://user-images.githubusercontent.com/31788091/229339589-a0a27947-13b2-4173-9e91-1076aca645ea.png)


<br/>

## Method_3 guide(Windows 10)

Requires Python3 and the paramiko, configparser, and tkinter modules.

``` 
pip install paramiko configparser
```

## Method_3 Example
#### Run `PFB.py`

![image](https://user-images.githubusercontent.com/31788091/229403056-b0499eb4-b157-4379-a32e-c3a7912926d6.png)

SSH connection information, except for the password, is then stored in `config.ini`

![image](https://user-images.githubusercontent.com/31788091/229403747-65024fd8-9b5c-4322-93f4-e81c9cab0cbf.png)

Then click the `PFB Tx` button to execute the PayForBlob transaction.

![image](https://user-images.githubusercontent.com/31788091/229403329-76115842-ed9b-4e93-977a-97ccf6eb836a.png)

![image](https://user-images.githubusercontent.com/31788091/229403345-9acc1d19-3326-430d-9074-b62efbf960a1.png)

That's it!


# PHASE 3 Guide
### This guide was written using Method 1 - CLI

``` 
wget https://raw.githubusercontent.com/inklbot/celestia-itn/main/blob.sh && sed -i 's/\r//' blob.sh && chmod +x blob.sh && sudo /bin/bash blob.sh
```

![image](https://user-images.githubusercontent.com/31788091/231226594-c5842947-6fae-4943-ac33-bc16b323f547.png)

![image](https://user-images.githubusercontent.com/31788091/231224969-ff6fcf3e-dd30-43d5-8588-50cd87e1fb36.png)

Using your web browser, navigate to the link below.

![image](https://user-images.githubusercontent.com/31788091/231227674-e52f60f7-4009-4f50-8298-8d0a9992c345.png)

Make sure the Status is Success, and the signer matches the Wallet Address listed in Celestia Knack - Account Settings

![image](https://user-images.githubusercontent.com/31788091/231225999-5ce275d4-3f96-4e89-903a-dac70bc295bd.png)

That's it!
If everything is perfect, submit your Tx Hash

### Errors

![image](https://user-images.githubusercontent.com/31788091/231235593-b81baa71-5b86-40ca-bffd-0653b6918cce.png)

`rpc error: code = NotFound desc ~` this error appears to be caused by the absence of assets in the wallet

