var submit = true;
// Make a fetch request to see if the coupon acutally exists and is valid or not
function check_coupon(coupon){
    var url = '/checkout/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'action':'check-coupon', 'coupon':coupon})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        valid = data['valid']
        if (valid == 'yes')
        {
            document.getElementsByClassName('alert-danger')[1].style.display = 'None';
        }
        else{
            document.getElementsByClassName('alert-danger')[1].style.display = 'block';
            // scroll to top
            document.body.scrollTop = 0;
            document.documentElement.scrollTop = 0;
            submit = false
        }
    })
    return submit;
}


var place_btn = document.getElementById('place-order-btn');
place_btn.addEventListener('click', function(e) {
    var submit = true;

    // Check if there is any coupon code
    // If there is check valid
    // If not valid, stop POST request and show the error
    var coupon = document.getElementById('checkout-discount-input');
    if (coupon.value == '')
    {
        coupon_code = coupon.value
    }
    else{
        submit = check_coupon(coupon.value);
        coupon_code = coupon.value
    }

    // Check if any compulsary form is left empty or not
    required_form = document.getElementsByClassName('required-form');
    for (i = 0; i < required_form.length; i++) {
        if (required_form[i].value == null || required_form[i].value == '') {
            required_form[i].style.border = "1px solid red";
            document.getElementsByClassName('alert-danger')[0].style.display = 'block';
            submit = false;

            // scroll to top
            window.scrollTo({ top: 0, behavior: 'smooth' });
        }
    }

    if (submit == true) {
        document.getElementsByClassName('alert-danger')[0].style.display = 'None';
        // Collect Billing Address data
        first_name = document.getElementById('bill_first_name').value;
        last_name = document.getElementById('bill_last_name').value;
        locality = document.getElementById('bill_locality').value;
        city = document.getElementById('bill_city').value;
        province = document.getElementById('bill_province').value;
        zipcode = parseInt(document.getElementById('bill_zipcode').value);
        phone = document.getElementById('bill_phone').value;
        alternative_phone_number = parseInt(document.getElementById('bill_alternative_phone_number').value);
        customer_pan_name = parseInt(document.getElementById('bill_customer_pan_number').value);

        // Collect Shipping Address data
        ship_first_name = document.getElementById('ship_first_name').value;
        ship_last_name = document.getElementById('ship_last_name').value;
        ship_locality = document.getElementById('ship_locality').value;
        ship_city = document.getElementById('ship_city').value;
        ship_province = document.getElementById('ship_province').value;
        ship_zipcode = parseInt(document.getElementById('ship_zipcode').value);
        ship_phone = document.getElementById('ship_phone').value;
        ship_alternative_phone_number = parseInt(document.getElementById('ship_alternative_phone_number').value);
        ship_pickup_address = document.getElementById('ship_pickup_address').value;
        ship_special_notes = document.getElementById('ship_special_notes').value;

        payment = document.getElementsByClassName('payment-method');

        for (i = 0; i < payment.length; i++) {
            if (payment[i].getAttribute('aria-expanded') == 'true') {
                payment_method = (payment[i].dataset.name)
            }
        }

        place_order(coupon_code,first_name, last_name, locality, city, province, zipcode, phone, alternative_phone_number, customer_pan_name, 
            ship_first_name, ship_last_name, ship_locality, ship_city, ship_province, ship_zipcode, ship_phone, ship_alternative_phone_number, ship_pickup_address, ship_special_notes,payment_method);

    }

})


place_order = (coupon_code,first_name, last_name, locality, city, province, zipcode, phone, alternative_phone_number, customer_pan_name, 
    ship_first_name, ship_last_name, ship_locality, ship_city, ship_province, ship_zipcode, ship_phone, ship_alternative_phone_number, ship_pickup_address, ship_special_notes,payment_method) => {
    var url = '/checkout/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'action':'checkout','coupon_code':coupon_code, first_name: first_name, 'last_name': last_name, 'locality': locality, 'city': city, 'province': province, 'zipcode': zipcode, 'phone': phone, 'alternative_phone_number': alternative_phone_number, 'customer_pan_number': customer_pan_name, 
        'ship_first_name': ship_first_name, 'ship_last_name': ship_last_name, 'ship_locality': ship_locality, 'ship_city':ship_city, 'ship_province': ship_province, 'ship_zipcode': ship_zipcode, 'ship_phone': ship_phone, 'ship_alternative_phone_number': ship_alternative_phone_number, 'ship_pickup_address': ship_pickup_address, 'ship_special_notes':ship_special_notes, 'payment_method': payment_method })
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        orderId = data['orderid']
        window.location.href = '/invoice/' + orderId + '/'
    })
}