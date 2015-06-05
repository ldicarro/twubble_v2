<?php

require_once('TwitterAPIExchange.php');

$settings = array(
    'oauth_access_token' 		=> "32311090-ARf4wFxaGgzK5EVuc62TdWU6oYTtqyKSCh0Dmo",
    'oauth_access_token_secret' => "Rm5vWH9kYvCoLAmoY58Upb9KaL2fJRdEPoIxikL4",
    'consumer_key' 				=> "Aw8UuSjja5hFJEjfH4VvbA",
    'consumer_secret' 			=> "QuvH9IJpFBRFb8idKBsO7Cq2hZ8X7BFBoqnnMmrEKQ"
);

$url = 				'https://api.twitter.com/1.1/search/tweets.json';
$getfield = 		'?q=%23thoughttwubble&include_entities=false';
$requestMethod = 	'GET';

$twitter = new TwitterAPIExchange($settings);
$response = $twitter->setGetfield($getfield)
					->buildOauth($url, $requestMethod)
					->performRequest();


//$json = file_get_contents("http://search.twitter.com/search.json?q=%23wwe&since_id=331969064274624512&callback=?", true); //getting the file content
$decode = json_decode($response, true); //getting the file content as array

echo html_entity_decode($decode['statuses'][0]['text'])."\n";
echo "@".$decode['statuses'][0]['user']['screen_name'];
//echo "<br />";
//var_dump($decode); //getting the file content as array
?>
