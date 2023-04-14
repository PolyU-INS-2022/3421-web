$(document).ready(function() {
    var credits = $('#end-credits');
    var divs = credits.children();
    var duration = 30;
  
    // Set the initial position of the credits
    credits.css('top', '100%');
  
    // Animate the credits infinitely
    function animateCredits() {
      divs.each(function(index) {
        $(this).delay(index * 1000).animate({ opacity: 0 }, 1000);
      });
  
      credits.animate({ top: '0%' }, duration * 1000, 'linear', function() {
        divs.css('opacity', 1);
        credits.css('top', '100%');
        animateCredits();
      });
    }
  
    animateCredits();
  });
  
  