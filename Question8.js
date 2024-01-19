// status code 200 
pm.test("Status code is 200", function () {

    pm.response.to.have.status(200);

});

[
    {
        "name": "Marywood University",
        "alpha_two_code": "US",
        "state-province": null,
        "domains": ["marywood.edu"],
        "country": "United States",
        "web_pages": ["http://www.marywood.edu"]
    }
]

// status code of 404 (Not Found)

pm.test("Status code is 404", function () {

    pm.response.to.have.status(404);

});

// <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
// <title>405 Method Not Allowed</title>
// <h1>Method Not Allowed</h1>
// <p>The method is not allowed for the requested URL.</p>


// ERROR 404 NOT FOUND ON API URL  http://universities.hipolabs.com/search?country=United+States
