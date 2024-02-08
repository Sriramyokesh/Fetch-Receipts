# Fetch-Receipts

## Running

Clone the project and get into ./src/ folder.
Run the following commands (Keep Docker daemon running):

```
docker build -t receiptapp .
docker run -p 5000:5000 receiptapp
```

Now, run http://127.0.0.1:5000/ to connect to the API.

You can use the fetch.py from /test/ folder or Postman or someother way to make the POST, GET calls.

## Assumptions

The following are some of the assumptions made for the calculation of points, where there were some ambiguities in the description.

10 points if the time of purchase is after 2:00pm and before 4:00pm.

This has been interpreted as 10 points for purchases from 2:00 pm to 3:59 pm, as there is no explicit specification of inclusive/exclusive interval. Generally, I have assumed that stores may have shifts, peak hours, etc. that would normally start at an hour and end before the next hour starts, thus, 2:00 pm to 3:59 pm.

## Testing

After running the commands,

![image](https://github.com/Sriramyokesh/Fetch-Receipts/assets/24229318/39f41441-310c-4093-ac0b-4704e9915f0b)

The server is now ready to accept requests on http://127.0.0.1:5000/

![image](https://github.com/Sriramyokesh/Fetch-Receipts/assets/24229318/6a63596f-9108-4788-b0f2-975c0e0b53bb)

1. We can use either /test/fetch.py (In a python 3 environment run, pip install requests followed by python fetch.py) (or)
2. Use Postman tool as follows:

### POST

![image](https://github.com/Sriramyokesh/Fetch-Receipts/assets/24229318/efd1e083-6bef-4e11-8f42-eadeacec0044)

### GET
![image](https://github.com/Sriramyokesh/Fetch-Receipts/assets/24229318/5f5e2761-175f-4265-863f-9a76d0e1b95a)

(or)
3. Use curl or some other means of communicating with the API


