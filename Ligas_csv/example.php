<?php 

// Grab All Data Here:

	// Matches Demo

	$matches = file_get_contents("https://api.footystats.org/league-matches?key=example&league_id=1625");
	$matches = json_decode($matches, true);
	$matches = $matches["data"];

	// League Table

	$leagueTable = file_get_contents("https://api.footystats.org/league-tables?key=example&league_id=1625");
	$leagueTable = json_decode($leagueTable, true);
	$leagueTable = $leagueTable['data']['all_matches_table_away'];

	// Match Limits

	$limit = 20;
	$counter = 0;

 ?>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
<style>
	body{
		padding: 2rem 0px;
		font-size: 12px;}
	table{
		font-size: 12px;}
	.mb2{margin-bottom: 1rem;}
</style>

<div class="container">

<!--
MATCHES LOOP
* Try building on this to add more stats and conditionals *
-->

<div class="row"><div class="col-lg-10 mx-auto">


<div class="row"><div class="col-lg-12">

<h4 class="mb2">Matches from EPL
<small class="text-muted">Limited to <?php echo $limit ?></small>
</h4>
<ul>

<?php

// Begin Loop

foreach ($matches as $match):	

	// If Past The Limit, Break

	if($counter > $limit):
		continue;
	endif;

	// Loop Through Games

	echo "{$match['home_name']} {$match['homeGoalCount']} - {$match['awayGoalCount']} {$match['away_name']}<br>";

	// Add to The Counter

	$counter++;

// End Loop

endforeach; 

?>

</ul>

</div>
<div class="col-lg-12">

<!--
LEAGUE TABLE OUTPUT
* Try adding more data points to this league table, like the amount of points? You can always take a look at the available stats by using print_r($leagueTable[0] for Manchester City); *
-->

<h4 class="mb2">Away League Table
<small class="text-muted">EPL 2018/2019</small>
</h4>

<table class="table table-bordered">

	<thead>
		<tr>
			<th>Team Name</th>
			<th>Played</th>
			<th>Won</th>
			<th>Drawn</th>
			<th>Lost</th>
		</tr>
	</thead>

	<tbody>
		<?php foreach ($leagueTable as $key => $team): ?>
			<tr>
				<td><?php echo $team['name'] ?></td>
				<td><?php echo $team['matchesPlayed'] ?></td>
				<td><?php echo $team['seasonWins'] ?></td>
				<td><?php echo $team['seasonDraws'] ?></td>
				<td><?php echo $team['seasonLosses_away'] ?></td>
			</tr>
		<?php endforeach ?>
	</tbody>
</table>


</div>
<div class="col-lg-12">

<h4 class="mb2">Filtered Games <small class="text-muted">BTTS & Strong Away Teams</small></h4>

<table class="table table-bordered">
	
	<thead>
		<tr>
			<th>Game</th>
			<th>AVG Goals</th>
			<th>BTTS %</th>
			<th>Date</th>
		</tr>
	</thead>

	<tbody>
		<?php foreach ($matches as $key => $match): ?>

<!-- Filter for certain rules and patterns -->

	<?php
	if ($match['btts_potential'] >= 65 && $match['away_ppg'] >= 1.50):
	else:
		// If not, skip this game
		continue;
	endif;
	?>

<!-- / End filters -->

			<tr>
				<td><?php echo $match['home_name'] ?> vs <?php echo $match['away_name'] ?></td>
				<td><?php echo $match['avg_potential'] ?></td>
				<td><?php echo $match['btts_potential'] ?>%</td>
				<td><?php echo gmdate('d,m,Y', $match['date_unix']) ?></td>
			</tr>
		<?php endforeach ?>
	</tbody>
</table>

</div>
</div>
</div>
</div>
</div>
