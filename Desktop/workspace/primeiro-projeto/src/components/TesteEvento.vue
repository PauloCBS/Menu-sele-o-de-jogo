<template>
    <div class="teste-evento">
        <h2>Teste evento</h2>´
       <p v-on:click = "deixarMaiscula">{{mensagem}}</p>
    </div>
</template>
	
<script>
export default{    
    name: 'TesteEvento',
    data(){
        return{
            mensagem: 'o rato roeu a roupa do rei de roma'
        }
    },
    methods: {
        deixarMaiscula(){
            this.mensagem = this.mensagem.toUpperCase();
        }
    }
}
</script>

<style scoped>
</style>
