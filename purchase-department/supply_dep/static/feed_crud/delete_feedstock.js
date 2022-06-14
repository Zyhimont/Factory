axios.defaults.headers.common['Content-Type'] = 'application/json';
axios.defaults.headers.common['Accept'] = 'application/json';

new Vue({
  el: "#delete-feed-form",
  data: {
  },
  methods: {
  	submitForm(pk){
      axios.delete('/api/feedstock/<int:pk>/')
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      })
    }
  }
})