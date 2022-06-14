axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.headers.common['Accept'] = 'application/json';

new Vue({
  el: "#create-feed-form",
  data: {
        feedstock: {
        name: this.name,
        amount: this.amount,
        cost: this.cost,
        general_expenses: this.general_expenses
      },
  },
  methods: {
  	submitForm(){
      axios.post('/api/feedstock/', feedstock)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      })
    }
  }
})