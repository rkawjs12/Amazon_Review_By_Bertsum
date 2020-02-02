<template>
   <div>
      <v-row v-if="page=='front'" >

        <v-btn rounded color="primary" dark style='margin-right: 10px' @click='bert_sum(1)' ><v-icon>mdi-star</v-icon></v-btn>
        <v-btn rounded color="primary" dark style='margin-right: 10px' @click='bert_sum(2)'><v-icon v-for='i in Array.from({length: 2}, (x,i) => i)' :key='i'>mdi-star</v-icon></v-btn>
        <v-btn rounded color="primary" dark style='margin-right: 10px' @click='bert_sum(3)'><v-icon v-for='i in Array.from({length: 3}, (x,i) => i)' :key='i'>mdi-star</v-icon></v-btn>
        <v-btn rounded color="primary" dark style='margin-right: 10px' @click='bert_sum(4)'><v-icon v-for='i in Array.from({length: 4}, (x,i) => i)' :key='i'>mdi-star</v-icon></v-btn>
        <v-btn rounded color="primary" dark @click='bert_sum(5)'><v-icon v-for='i in Array.from({length: 5}, (x,i) => i)' :key='i'>mdi-star</v-icon></v-btn>

        <v-col cols="12" md="12">
          <v-textarea
            outlined
            name="input-7-4"
            label="내용"
            v-model='text1'
            rows='30'
            height='600'
          ></v-textarea>
          <v-btn color="success" dark large @click='review()' style="margin-right: 100px" >review</v-btn>
          <v-btn color="error" dark large @click='real_bert_sum()' >본문 줄여!</v-btn>
        </v-col>
        
        <loading :active.sync="isLoading" 
          :can-cancel="true" 
          background-color='#555555'
          :opacity='0.8'
          :on-cancel="onCancel"
          :is-full-page="fullPage">
        </loading>
        <v-snackbar
          v-model="snackbar"
          :multi-line="multiLine"
        >
          {{ text }}
          <v-btn
            color="red"
            text
            @click="snackbar = false"
          >
            Close
          </v-btn>
        </v-snackbar>
      </v-row>


      <v-row v-if="page=='result'" >
        <v-btn rounded color="primary" dark style='margin-right: 10px' @click="page='front'">뒤로</v-btn>


        <v-card
            max-width="100%"
            class="mx-auto"
            style="margin-top: 30px"
          >
            <v-list-item>
              <v-list-item-content>
                <v-list-item-title class="headline">결과</v-list-item-title>
                <v-list-item-subtitle>by 글버트</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>

            <v-img
              :src="img"
              v-if="img!=''"
            ></v-img>

            <v-card-text v-text='text2' style='align: justify'>
              Visit ten places on our planet that are undergoing the biggest changes today.
            </v-card-text>


          </v-card>  


      </v-row>  
     
   </div>



</template>

<script>
import Loading from 'vue-loading-overlay';
import 'vue-loading-overlay/dist/vue-loading.css';

export default {
  data () {
    return {
      page: 'front',
      current_page: 1,
      isLoading: false,
      fullPage: true,
      text1: ``,
      text2: '',
      multiLine: true,
      snackbar: false,
      text: '내용이 없습니다',
      img: ''
    }
  },
  mounted(){
    // this.$axios.get('http://localhost:5000/testpage')
    // .then(result=>{
    //   console.log(result);
    // })
  },

  methods: {
    onCancel() {
      console.log('User cancelled the loader.')
    },

    real_bert_sum(){
      if(this.text1!=''){
        const data = { data: this.text1} 
        this.isLoading = true
        this.$axios.post('http://localhost:5000/real_bert_sum', data)
        .then(result=>{
          if(result){
            this.isLoading = false;
            this.page = 'result'
            this.text2 = result.data.answer
            this.img = ''
          }
        })
      }else{
        this.snackbar = true
      }

    },

    review(){
      this.$axios.post('http://localhost:5000/review', {file: this.current_page})
        .then(result=>{
          if(result){
            console.log(result);
            this.isLoading = false;
            this.page = 'result'
            this.text2 = result.data.result
            this.img = result.data.img
          }
        })

    },

    bert_sum(option){
      this.current_page = option
      const data = { data: this.text1, file: option } 
      console.log(data);
        this.isLoading = true
        this.$axios.post('http://localhost:5000/bert_sum', data)
        .then(result=>{
          console.log(result);
          if(result){
            this.isLoading = false;
            this.text1 = result.data.result
          }
        })
    }
  },

  components: {
    Loading
  }
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.title {
  font-family: 'Quicksand', 'Source Sans Pro', -apple-system, BlinkMacSystemFont,
    'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}
</style>
