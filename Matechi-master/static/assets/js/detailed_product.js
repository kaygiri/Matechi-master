var final_rating;
// Render the ratings first
$(".my-rating").starRating({
    totalStars: 5,
    starSize: 20,
    strokeWidth : 0,
    strokeColor : '#FFD700',
    emptyColor: 'lightgray',
    activeColor: 'orange',
    useGradient: false,
    readOnly: true
  });

  $(".set-rating").starRating({
    totalStars: 5,
    starSize: 30,
    strokeWidth : 0,
    strokeColor : 'orange',
    emptyColor: 'lightgray',
    activeColor: 'orange',
    useGradient: true,
    readOnly: false,
    disableAfterRate: false,
    onHover: function(currentIndex, currentRating, $el){
      $('.live-rating').text(currentIndex);
    },
    onLeave: function(currentIndex, currentRating, $el){
      $('.live-rating').text(currentRating);
    },
    callback: function(currentRating, $el){
      final_rating = currentRating;
    }
  });

  // Submit the review
  var sub = document.getElementById('submit-review-btn');
  sub.addEventListener('click', function(e){
    submit_review();
  })

  submit_review = ()=>{
    rating = final_rating;
    if (parseInt(rating) == 0)
    {
      submit = false;
    }
    else
    {
      submit = true;
    }
    full_name = document.getElementById('inputfullname').value;
    if (full_name == '')
    {
      submit = false;
    }
    else{
      submit = true;
    }
    review = document.getElementById('review').value;
    if (review == '')
    {
      submit = false;
    }
    else
    {
      submit = true;
    }
    productId = document.getElementById('submit-review-btn').getAttribute('data-productId');

    if (submit == true)
    {
      submit_to_server(rating,full_name,review, productId);
    }
    else
    {
      document.getElementsByClassName('review-error')[0].style.display = 'block';
    }
  }

  submit_to_server = (rating, full_name, review, productId) =>{
    var url = '/review/'

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body: JSON.stringify({'rating':rating, 'full_name': full_name, 'review' : review, 'productid' : productId})
    })
    .then((response) => {
        return response.json();
    })
    .then((data) => {
        valid = data['valid']
        if (valid == 'yes')
        {
          $('#myModal').modal('hide');
          $('#success').modal('show');
        }
        else{
        message = data['message'] 
        document.getElementById('sorry-msg').textContent = message;
        $('#myModal').modal('hide');
        $('#fail').modal('show');
        }
    })
    return submit;
  }

  $(".my-ratings-val").starRating({
    totalStars: 5,
    starSize: 18,
    strokeWidth : 0,
    strokeColor : '#FFD700',
    emptyColor: 'lightgray',
    activeColor: 'orange',
    useGradient: false,
    readOnly: true
  });