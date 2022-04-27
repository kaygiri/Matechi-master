var submit = true;

// Render CPU parts first
processor_name = JSON.parse(localStorage.getItem('processor_name'));
processor_price = JSON.parse(localStorage.getItem('processor_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = processor_name + '   X 1';
td2.innerHTML = 'Rs : ' + processor_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

motherboard_name = JSON.parse(localStorage.getItem('motherboard_name'));
motherboard_price = JSON.parse(localStorage.getItem('motherboard_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = motherboard_name + '   X 1';
td2.innerHTML = 'Rs : ' + motherboard_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

graphics_name = JSON.parse(localStorage.getItem('graphics_name'));
graphics_price = JSON.parse(localStorage.getItem('graphics_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = graphics_name + '   X 1';
td2.innerHTML = 'Rs : ' + graphics_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

ram_name = JSON.parse(localStorage.getItem('ram_name'));
ram_price = JSON.parse(localStorage.getItem('ram_price'));
ram_quantity = JSON.parse(localStorage.getItem('ram_quantity'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = ram_name + '   X ' + ram_quantity;
td2.innerHTML = 'Rs : ' + parseInt(ram_price) * parseInt(ram_quantity);
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

primary_name = JSON.parse(localStorage.getItem('primary_name'));
primary_price = JSON.parse(localStorage.getItem('primary_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = primary_name + '   X 1';
td2.innerHTML = 'Rs : ' + primary_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

secondary_name = JSON.parse(localStorage.getItem('secondary_name'));
secondary_price = JSON.parse(localStorage.getItem('secondary_price'));
secondary_quantity = JSON.parse(localStorage.getItem('secondary_quantity'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = secondary_name + '   X ' + secondary_quantity;
td2.innerHTML = 'Rs : ' + parseInt(secondary_price) * parseInt(secondary_quantity);
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

case_name = JSON.parse(localStorage.getItem('case_name'));
case_price = JSON.parse(localStorage.getItem('case_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = case_name + '   X 1';
td2.innerHTML = 'Rs : ' + case_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

cooler_name = JSON.parse(localStorage.getItem('cooler_name'));
cooler_price = JSON.parse(localStorage.getItem('cooler_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = cooler_name + '   X 1';
td2.innerHTML = 'Rs : ' + cooler_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

psu_name = JSON.parse(localStorage.getItem('psu_name'));
psu_price = JSON.parse(localStorage.getItem('psu_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = psu_name + '   X 1';
td2.innerHTML = 'Rs : ' + psu_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);

total_price = JSON.parse(localStorage.getItem('total_price'));
tr = document.createElement('tr');
td = document.createElement('td');
td2 = document.createElement('td');
td.innerHTML = 'Total :';
td2.innerHTML = 'Rs : ' + total_price;
tr.appendChild(td);
tr.appendChild(td2);
document.getElementById('product_list').appendChild(tr);





// Make a fetch request to see if the coupon acutally exists and is valid or not
function check_coupon(coupon){
    var url = '/custom-pc-nepal/checkout/'

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

        // Get the products
        processor_id = JSON.parse(localStorage.getItem('processor_id'));
        motherboard_id = JSON.parse(localStorage.getItem('motherboard_id'));
        graphics_id = JSON.parse(localStorage.getItem('graphics_id'));
        ram_id = JSON.parse(localStorage.getItem('ram_id'));
        ram_quantity = JSON.parse(localStorage.getItem('ram_quantity'));
        primary_id = JSON.parse(localStorage.getItem('primary_id'));
        secondary_id = JSON.parse(localStorage.getItem('secondary_id'));
        secondary_quantity = JSON.parse(localStorage.getItem('secondary_quantity'));
        case_id = JSON.parse(localStorage.getItem('case_id'));
        cooler_id = JSON.parse(localStorage.getItem('cooler_id'));
        psu_id = JSON.parse(localStorage.getItem('psu_id'));

        payment = document.getElementsByClassName('payment-method');

        for (i = 0; i < payment.length; i++) {
            if (payment[i].getAttribute('aria-expanded') == 'true') {
                payment_method = (payment[i].dataset.name)
            }
        }

        place_order(coupon_code,first_name, last_name, locality, city, province, zipcode, phone, alternative_phone_number, customer_pan_name, 
            ship_first_name, ship_last_name, ship_locality, ship_city, ship_province, ship_zipcode, ship_phone, ship_alternative_phone_number, ship_pickup_address, ship_special_notes,
            processor_id, motherboard_id, graphics_id, ram_id, ram_quantity, primary_id, secondary_id, secondary_quantity, case_id, cooler_id, psu_id,payment_method);

    }

})


place_order = (coupon_code,first_name, last_name, locality, city, province, zipcode, phone, alternative_phone_number, customer_pan_name, 
    ship_first_name, ship_last_name, ship_locality, ship_city, ship_province, ship_zipcode, ship_phone, ship_alternative_phone_number, ship_pickup_address, ship_special_notes,
    processor_id, motherboard_id, graphics_id, ram_id, ram_quantity, primary_id, secondary_id, secondary_quantity, case_id, cooler_id, psu_id,payment_method) => {
        var url = '/custom-pc-nepal/checkout/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'action':'checkout','coupon_code':coupon_code, first_name: first_name, 'last_name': last_name, 'locality': locality, 'city': city, 'province': province, 'zipcode': zipcode, 'phone': phone, 'alternative_phone_number': alternative_phone_number, 'customer_pan_number': customer_pan_name, 
        'ship_first_name': ship_first_name, 'ship_last_name': ship_last_name, 'ship_locality': ship_locality, 'ship_city':ship_city, 'ship_province': ship_province, 'ship_zipcode': ship_zipcode, 'ship_phone': ship_phone, 'ship_alternative_phone_number': ship_alternative_phone_number, 'ship_pickup_address': ship_pickup_address, 'ship_special_notes':ship_special_notes, 
        'processor_id' : processor_id, 'motherboard_id' : motherboard_id, 'graphics_id' : graphics_id, 'ram_id' : ram_id, 'ram_quantity' : ram_quantity, 'primary_id' : primary_id, 'secondary_id' : secondary_id, 'secondary_quantity' : secondary_quantity, 'case_id' : case_id, 'cooler_id' : cooler_id, 'psu_id' : psu_id, 'payment_method': payment_method })
    })

    .then((response) => {
        return response.json();
    })

    .then((data) => {
        orderId = data['orderid']
        link = window.location.origin + '/invoice/' + orderId + '/';
        window.location.href = (link);
    })
}