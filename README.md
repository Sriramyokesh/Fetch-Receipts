# Fetch-Receipts

## Running

Clone the project and get into /src/ folder.
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

