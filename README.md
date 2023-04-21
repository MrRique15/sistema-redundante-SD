This project uses FastAPI and uvicorn to create a distributed sistem that has redundancy:<br/>

---

> Initial Steps:<br/>

What do you need to run this project?<br/>

For first, you need to install Python 3.8 or higher. You can download it from [here](https://www.python.org/downloads/).<br/>
Then, you need to create a virtual environment. You can do it by running the following command:<br/>

```console
$ python -m venv env
```

Now, with the virtual environment created, you need to activate it. You can do it by running the following command:<br/>

```console
$ env/Scripts/activate
```

With the environment activated, you need to install the dependencies. You can do it running the following command :<br/>

```console
$ pip install -r requirements.txt
```
---

> Starting Servers:<br/>

Now, to run it, you need to stay into the project folder and run the following commands:<br/>

For main server, specify the port you want, any port is accepted.<br/>

```console
$ python main-server/main.py <port>
```

Now, for the processing servers, run the following command, alternating the port number. Ports accpeted[7771,7772,7773]:<br/>
```console
$ python processing-server/processing.py <port>
```

Now, the API is running on your [localhost](http://localhost:7779) by default with the port 7779.<br/>

You can acess the API documentation by accessing the following link: [http://localhost:7779/docs](http://localhost:7779/docs)<br/>
FastAPI will generate the documentation automatically.<br/>

---

> Testing:<br/>

You can test the API using [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/download).<br/>

---

> Explanation:<br/>

The main server is responsible for receiving the requests and sending them to the corresponding processing servers.<br/>
The processing servers are responsible for processing the requests and sending the response back to the main server.<br/>
And then the main server will send the response back to the client.<br/>

The main servers analyze the requests and the status of the processing servers.<br/>
For first, it tryes to send the request to the processing server on port `7771`, if it isn´t available, the main server will try sendding to processing server with por `7772` or `7773`.<br/>
If the three processing servers are unavailable, the main server will send a message to the client saying that the servers are unavailable.<br/>

![image](https://user-images.githubusercontent.com/61984488/233520363-894c3512-ec12-4b54-be1a-653c92975407.png)

---
Enjoy it! :D
