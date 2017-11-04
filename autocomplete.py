import webapp2
import json

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("""
<html>
<head>
<link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/themes/smoothness/jquery-ui.css">
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.12.1/jquery-ui.min.js"></script>
<script>
  $( function() {
    function log( message ) {
      $( "<div>" ).text( message ).prependTo( "#log" );
      $( "#log" ).scrollTop( 0 );
    }

    $( "#animals" ).autocomplete({
      source: "./products",
      minLength: 2,
      select: function( event, ui ) {
        log( "Selected: " + ui.item.value + " aka " + ui.item.id  );
      }
    });
  } );
</script>
</head>
<body>
<div class="ui-widget">
  <label for="animals">Animals: </label>
  <input id="animals">
</div>

<div class="ui-widget" style="margin-top:2em; font-family:Arial">
  Result:
  <div id="log" style="height: 200px; width: 300px; overflow: auto;" class="ui-widget-content"></div>
</div>
</body>
</html>
""")

class Products(webapp2.RequestHandler):
    def get(self):
        term = self.request.get('term', None)
        self.response.headers['Content-Type'] = 'application/json'
        data = ['cat', 'dog', 'bird', 'wolf']
        if term: 
            data = [{"label":i, "id":i + "_id"} for i in data if i.find(term) >= 0 ]
        data = json.dumps(data)
        self.response.out.write(data)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/products', Products),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host="0.0.0.0", port="8080")

if __name__ == '__main__':
    main()
