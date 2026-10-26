---
id: "43546507545879"
titulo: "Erro eSocial S-2206 - Não gera evento de alteração de função do colaborador"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/43546507545879-Erro-eSocial-S-2206-N%C3%A3o-gera-evento-de-altera%C3%A7%C3%A3o-de-fun%C3%A7%C3%A3o-do-colaborador"
trilha: "Solução de Problemas > Pessoal+"
atualizado_em: "2026-09-18T11:09:15Z"
rotulos: ["Artigo criado KCS", "Sankhya RH - KCS"]
---

# Erro eSocial S-2206 - Não gera evento de alteração de função do colaborador

**MENSAGEM**

O sistema não apresenta mensagem de erro específica, mas ao tentar gerar o evento S-2206 (Alteração Contratual) referente à alteração de função ou cargo do colaborador, o evento não é gerado para envio ao eSocial.

**SITUAÇÃO**

Ao realizar uma alteração de função ou cargo no cadastro do colaborador (Configurações Cadastros Parceiros), espera-se que o sistema gere automaticamente o evento S-2206 para envio ao eSocial. No entanto, após a alteração, o evento não aparece na lista de eventos pendentes para o colaborador, impossibilitando o envio da informação ao governo.

**Principais Causas**

1. **Situação do eSocial Incorreta no Cadastro do Funcionário**
   - Se o campo “Situação no eSocial” estiver configurado como “Oficial: S-2200 e S-2300”, o sistema não gera o S-2206.
2. **Data de Alteração Anterior à Obrigatoriedade do eSocial**
   - O sistema não gera eventos com data anterior à data de início da obrigatoriedade do eSocial para a empresa.
3. **Eventos Posteriores na Linha do Tempo**
   - Se existem eventos S-2205, S-2206 ou S-2230 com data posterior à alteração, o novo evento pode não ser gerado.
4. **Funcionário Afastado**
   - Para funcionários afastados, algumas alterações podem não gerar gatilho para o S-2206, dependendo do tipo de afastamento.

**SOLUÇÃO**

**(1)** Verifique se a alteração de função ou cargo foi realizada corretamente na tela de cadastro do colaborador, preenchendo todos os campos obrigatórios, especialmente a data da alteração e o novo cargo ou função.

**(2)** Ao salvar a alteração, observe se o sistema exibe o pop-up para informar a data da alteração e se a opção marcada é **"Inclusão de nova alteração contratual"**. Caso a alteração já tenha sido enviada anteriormente para a mesma data, marque **"Retificação de alteração contratual já enviada ao eSocial"**.

**(3)** Confirme se não existem eventos S-2206 ou S-2205 já enviados para a mesma data. Caso existam, o sistema pode entender que não há necessidade de novo envio, a menos que seja uma retificação.

Acesse a “Central do eSocial”: `Pessoal+ » Rotinas Folha » Central do eSocial`

Utilize o código de recibo ou filtros para localizar eventos S-2205, S-2206 ou S-2230 com data posterior à alteração desejada.

Se existirem, exclua ou retifique esses eventos para liberar a linha do tempo.

**(4)** Acesse o portal do eSocial, consulte o CPF do colaborador e verifique as movimentações trabalhistas para identificar se já existe um evento de alteração contratual para a data desejada.

**(5)** Se necessário, ajuste a data da alteração no sistema para uma data diferente da já enviada, ou realize a retificação conforme o caso. Após o ajuste, gere novamente o evento S-2206 e envie ao eSocial.

**CAUSA**

A não geração do evento S-2206 ocorre, geralmente, porque já existe um evento de alteração contratual (S-2206) ou cadastral (S-2205) enviado para a mesma data da alteração realizada, ou porque a alteração não foi corretamente registrada no sistema, como por exemplo, a falta de preenchimento da data ou do novo cargo. O sistema, ao identificar que não há mudança efetiva ou que a data já foi utilizada, não gera novo evento para evitar duplicidade de informações no eSocial.
