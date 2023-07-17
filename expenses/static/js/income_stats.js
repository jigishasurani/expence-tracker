const renderChart = (data, labels) => {
    var ctx = document.getElementById("myChart").getContext("2d");
    var myChart = new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [
          {
            label: "Last 6 months Income",
            data: data,
            backgroundColor: [
                "violet",
                "darkorange",
                "darkgrey",
                "lightgreen",
                "lightskyblue"
            ],
            borderColor: [
              "darkmagneta",
              "maroon",
              "black",
              "green",
              "blue"
            ],
            borderWidth: 2,
            innerWidth: 3,
          },
        ],
      },
      options: {
        title: {
          display: true,
          text: "Income per Source",
        },
      },
    });
  };
  
  const getChartData = () => {
    console.log("fetch");
    fetch("income_source_summary")
      .then((res) => res.json())
      .then((results) => {
        console.log("results", results);
        const source_data = results.income_source_data;
        const [labels, data] = [
          Object.keys(source_data),
          Object.values(source_data),
        ];
  
        renderChart(data, labels);
      });
  };
  
  document.onload = getChartData();