
function kGuage(ctx, values){
	var idata = {
		labels: [
			"Empty",
			"Full"
		],
		datasets: [
			{
				data: values,
				backgroundColor: [
					"#aaaaaa",
					"#36A2EB"
				]
			}
		]
	};

	var opt = {
	  //responsive: true,
	  legend: {
		display: false
	  },
	  circumference: 1.5*Math.PI,
	  rotation: 0.750*Math.PI
	};

	var config = {
		type: 'doughnut',
		data: idata,
		options: opt
	}

	var mychart = new Chart(ctx, config);

	return mychart;
};

function Legs(ctx, values){

	var colors = [
		"#2ecc71",
		"#3498db",
		"#9b59b6"
	];

	var config = {
		type: 'doughnut',
		options: {
			legend: {
				display: false
			},
			cutoutPercentage: 20
		},
		data: {
			labels: ["coxia", "femur", "tibia"],
			datasets: [
				{
					label: "hi1",
					backgroundColor: colors,
					data: values[0]
				},
				{
					label: "hi2",
					backgroundColor: colors,
					data: values[1]
				},
				{
					label: "hi3",
					backgroundColor: colors,
					data: values[2]
				},
				// {
				// 	backgroundColor: colors,
				// 	data: values[3]
				// }
			]
		}
	};

	var myChart = new Chart(ctx, config);
	return myChart;
}
