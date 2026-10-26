---
id: "42427346320919"
titulo: "Como criar um alerta de proposta sem atualização a X dias?"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/42427346320919-Como-criar-um-alerta-de-proposta-sem-atualiza%C3%A7%C3%A3o-a-X-dias"
trilha: "PLOOMES: Automação de propostas  > Automações"
atualizado_em: "2026-08-10T18:00:19Z"
rotulos: ["sync_hc", "ploomes", "ploomes_5452239", "sync_hash_bc4c0e71a397"]
---

# Como criar um alerta de proposta sem atualização a X dias?

Manter o controle sobre propostas sem atualização é essencial para não perder oportunidades no funil. Com as automações do Ploomes, é possível criar alertas automáticos e garantir um acompanhamento mais eficiente dos negócios.

## Configuração

## 1. Acessar as automações de Proposta

- Vá em **Administração > Automações**.
- Selecione a entidade **Proposta**.
- Clique em **Nova automação**.

[GIF animado: Imagem 1: Clique em Nova automação .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2507591069/2247529a02f712ac077a46f0c8df/msedge_H3sMGSpg0j.gif?expires=1786536000&signature=2f396ccceab9535b100c74b74fba87d881eb76eb7f24ac8a9696b95efd2832d7&req=diUnEcx3nIFZUPMW3nq%2BgW8oQ8fMVI%2B3%2BvCmfSoV%2B%2FLiWDtquVzRlriuKRR5%0AZoIu7rR%2F6dlSBJuH6VBrqudLGzk%3D%0A)

## 2. Criar a automação para registrar a última atualização

- Na **Descrição**, informe o objetivo da automação.
  Ex.: **Preencher a data da última atualização da proposta**.
- No **gatilho**, selecione **Quando o item for editado**.

  Neste caso, não é necessário adicionar filtro, pois a automação deve ser executada sempre que houver qualquer alteração na proposta.

[GIF animado: Imagem 2: Neste caso, não é necessário adicionar filtro, pois a automação deve ser executada sempre que houver qualquer alteração…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2507590788/48f4bbfe91a6ec6403d8a10b433c/msedge_FfSpOblTY9.gif?expires=1786536000&signature=207973ff9c344033f9f9b73eb008ec797e07dc4aff56dc6c356bd2896c36e1a2&req=diUnEcx3nYZXUfMW3nq%2Bgegm0LJEk8NzVAuED8xJS5LFwCsw%2B6ShD4%2B3Be0H%0AOAPeigE%2F4QHH8T%2Bio8WKslrGnTs%3D%0A)

## 3. Definir a ação de preenchimento da data

- Em **Ao ser disparada, o que a automação deve fazer?**, selecione **Editar dados**.
- No campo a ser preenchido, crie um novo campo, caso ele ainda não exista.
  Ex.: **Última atualização**.
- Defina esse campo como do tipo **Data**.
- Em **Tipo de preenchimento**, selecione **Dias após automação**.
- Preencha com o valor **0**, para que o campo receba a data atual no momento em que a automação for executada.
- No final, clique em salvar a automação

Neste caso, o valor **0** representa o dia atual. Assim, sempre que a proposta for editada, o campo **Última atualização** será atualizado automaticamente.

[GIF animado: Imagem 3: Neste caso, o valor 0 representa o dia atual. Assim, sempre que a proposta for editada, o campo Última atualização será…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221105447/0a0a6b2110f075a234b246d3a8f1/msedge_AxLHs8Nkua.gif?expires=1786536000&signature=ddf9a838191154d524d31c0e611c59082f81f022f69924ae30ab0624b227c77c&req=diIlF8h%2BmIVbXvMW3nq%2BgUH9wtPcklnR1JYqkftOUFWML2YrC9JKkxVCDc%2Bo%0AfT8thBjLTRtwycucO6wxCVOS8Ks%3D%0A)

## 4. Criar a automação de alerta periódico

- Ainda na entidade **Proposta** na tela de automações, clique em **Nova automação**.
- Na **Descrição**, informe o objetivo da automação.
  Ex.: **Criar alerta de proposta sem atualização há 10 dias**.
- No **gatilho**, selecione **Periodicamente**.
- Configure a execução para ocorrer **todos os dias**.
- Defina a data de início e o horário desejado para a verificação.
  Ex.: iniciar hoje, às **00:00**.

[GIF animado: Imagem 4: Defina a data de início e o horário desejado para a verificação. Ex.: iniciar hoje, às 00:00 .](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221114898/1168aab264f652eb02f025aa3243/msedge_isRhMsBoJT.gif?expires=1786536000&signature=57dc1120c38af4898e7149520fc362e23ed62150975383338522c9c988456fe6&req=diIlF8h%2FmYlWUfMW3nq%2BgbYVXX%2BUGfy02ibwGuxk1dmrtrQzHBR546MlaY1T%0AkSwxqkkg4eZd41OsQYZq06Bf%2FYg%3D%0A)

## 5. Configurar o filtro da automação

Adicione os seguintes critérios para identificar apenas as propostas cuja última atualização ocorreu exatamente há 10 dias:

- **Última atualização** = **Data relativa > Últimos n dias** = **10**
- **Última atualização** ≠ **Data relativa > Últimos n dias** = **9**

Essa combinação é importante para que a automação considere apenas o dia exato de 10 dias atrás, e não todo o intervalo dos últimos 10 dias.

[GIF animado: Imagem 5: Essa combinação é importante para que a automação considere apenas o dia exato de 10 dias atrás, e não todo o intervalo…](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221119505/a1c0a5a026c9b5c5a505b478274f/msedge_XdFoTFHy1L.gif?expires=1786536000&signature=82c073e9d4fa090152c41c4cff9ca4b8398b6a54e94441097b58ff74777aaaab&req=diIlF8h%2FlIRfXPMW3nq%2BgQDqP6qVkpm5IEJicXDXXx%2B4H49M8fv1G1YVvBpb%0A8r6vec9HuN7lPlY2BoBARk8FgxU%3D%0A)

## 6. Definir a ação do alerta e configurar os dados da tarefa

Em **Ao ser disparada, o que a automação deve fazer?**, selecione **Criar tarefa**.

Você também pode optar por outras ações, como enviar um e-mail ou registrar uma interação, mas neste exemplo utilizarei a criação de tarefa.

Preencha os campos da tarefa conforme a necessidade. Exemplo:

- **Usuário**: responsável da proposta
- **Tipo**: simples
- **Título**: Proposta sem atualização há 10 dias
- **Descrição**: Por favor, verifique esta proposta
- Clique em **Salvar** para concluir.

Na **data de vencimento**, altere de valor estático para **Dias após automação** e preencha com o valor desejado.
Ex.: **5**

Neste caso, a tarefa será criada com vencimento para 5 dias após a execução da automação.

[GIF animado: Imagem 6: Neste caso, a tarefa será criada com vencimento para 5 dias após a execução da automação.](https://downloads.intercomcdn.com/i/o/kg4ewnrl/2221124826/abff1f4d9d2bcf083367fdbf4b81/msedge_BzwmPNmbJE.gif?expires=1786536000&signature=06c0ed6a96f8bc0edbf284b31619c0bae46fda2630cce2e9039b6239aede677a&req=diIlF8h8mYldX%2FMW3nq%2BgVoaWe%2F8emxUOxCI0jwFz7Z0jkN0qE9J1zsCUn3j%0ALUZXByZrOsMZlqQEo3%2FkM0dIxwI%3D%0A)

Após isso, a automação passará a verificar diariamente quais propostas estão há 10 dias sem atualização e criará a tarefa de alerta conforme configurado.

⚠️ Essa automação pode ser executada mais de uma vez para a mesma proposta, pois ela sempre considera o valor mais recente do campo **Última atualização**. Assim, se a proposta for alterada novamente e depois permanecer mais 10 dias sem edição, ocorrerá um novo alerta.

---

**Este artigo te ajudou?** Deixe seu retorno abaixo para continuarmos sempre melhorando nossa base de conhecimento. 😊

**Ficou com alguma dúvida?** Não hesite em chamar o Suporte pelo chat da plataforma ou pelo e-mail [suporte@ploomes.com](mailto:suporte@ploomes.com).
