document.addEventListener('DOMContentLoaded', function () {
    var usarSaltGenericoCheckbox = document.getElementById('usarSaltGenerico');
    var saltPersonalizadoInput = document.getElementById('saltPersonalizado');
    var quantidadeCaracteresInput = document.getElementById('quantidadeCaracteres');
    var saltPersonalizadoLabel = document.querySelector('label[for="saltPersonalizado"]'); // Selecionar o rótulo do campo SALT Personalizado

    // Função para atualizar a visibilidade do campo "SALT Personalizado" e o rótulo
    function updateSaltPersonalizadoInput() {
        if (usarSaltGenericoCheckbox.checked) {
            saltPersonalizadoInput.style.display = 'none';
            saltPersonalizadoInput.value = ''; // Limpar o campo
            saltPersonalizadoLabel.style.display = 'none'; // Ocultar o rótulo
        } else {
            saltPersonalizadoInput.style.display = 'block';
            saltPersonalizadoLabel.style.display = 'block'; // Exibir o rótulo
        }
    }

    // Chame a função quando a página carregar e quando a caixa de seleção mudar
    updateSaltPersonalizadoInput();
    usarSaltGenericoCheckbox.addEventListener('change', updateSaltPersonalizadoInput);

    document.getElementById('gerarToken').addEventListener('click', function () {
        var quantidadeCaracteres = quantidadeCaracteresInput.value;
        var usarSaltGenerico = usarSaltGenericoCheckbox.checked;
        var saltPersonalizado = saltPersonalizadoInput.value;

        // Enviar configurações para o backend
        axios.post('/generate_token', {
            quantidadeCaracteres: quantidadeCaracteres,
            usarSaltGenerico: usarSaltGenerico,
            saltPersonalizado: saltPersonalizado
        })
        .then(function (response) {
            // Atualizar os resultados na página
            document.getElementById('resultadoToken').textContent = response.data.token;
            document.getElementById('resultadoSalt').textContent = response.data.salt;
            // Simples exemplo de criptografia, substitua por sua implementação real
            var tokenCriptografado = btoa(response.data.token + response.data.salt);
            document.getElementById('resultadoCriptografado').textContent = tokenCriptografado;
        })
        .catch(function (error) {
            console.error(error);
        });
    });

    // function mostrarValor(valor) {
    //     document.getElementById('demo').textContent = valor;
    // }
});
