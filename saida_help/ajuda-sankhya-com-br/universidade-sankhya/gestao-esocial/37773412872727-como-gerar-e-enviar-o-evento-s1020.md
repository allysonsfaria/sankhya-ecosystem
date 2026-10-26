---
id: "37773412872727"
titulo: "Como gerar e enviar o evento S1020"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37773412872727-Como-gerar-e-enviar-o-evento-S1020"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:43Z"
rotulos: ["Configuração", "Eventos", "Impostos", "Folha", "eSocial", "Central do eSocial"]
---

# Como gerar e enviar o evento S1020

| Categoria |
| --- |
| [O que é o Evento S1020?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773412872727-Como-gerar-e-enviar-o-evento-S1020#h_01KFB1M151ZZH4G73GVRK3Q0CT) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773412872727-Como-gerar-e-enviar-o-evento-S1020#h_01KFB1KQF9N1QN41BFMQ98WNZM) |
| [Conferência do registro da empresa no módulo Pessoal](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773412872727-Como-gerar-e-enviar-o-evento-S1020#h_01KFB1KAEZTXZG8FGN7GDJN9SY) |
| [Conferência do registro fiscal da empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773412872727-Como-gerar-e-enviar-o-evento-S1020#h_01KFB1K4AKRAQWC08CPH8D2B2F) |
| [Geração e envio do evento S1020](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773412872727-Como-gerar-e-enviar-o-evento-S1020#h_01KFB1JZH5GZBHZCTJF5CNKTYW) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37773412872727-Como-gerar-e-enviar-o-evento-S1020#h_01KFB1JKR25SPHG0BCA1JK4VSR) |

## Evento S1020 - Lotações Tributárias

#### O que é o Evento S1020?

O evento S-1020 é responsável por registrar no eSocial as informações tributárias relacionadas às lotações da empresa — ou seja, ele define como os encargos trabalhistas e previdenciários (como INSS, FGTS e contribuições a terceiros) serão apurados por centro de custo, departamento, filial ou tomador de serviço. Nesse evento, são enviados dados como o código interno da lotação, o CNPJ do estabelecimento, o código FPAS, os códigos de entidades como SENAI e SEBRAE (terceiros), além de informações sobre desoneração da folha, substituição de contribuição e processos judiciais vinculados à tributação. Em resumo, o S-1020 organiza a estrutura de recolhimento de encargos dentro da empresa, garantindo que cada parte da operação esteja corretamente vinculada à sua responsabilidade tributária.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1112988986)

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

Siga as orientações indicadas abaixo para executar o evento S1020 em sua base de testes.

1. ##### Conferência do registro da empresa no módulo Pessoal

**Acesse**: Configurações » Cadastros »  Pessoal » Empresas

- O campo Tipo de lotação deve estar preenchido corretamente.

2. ##### Conferência do registro fiscal da empresa

**Acesse**: Pessoal+  » Cadastros »  Registro Fiscal

- Localize os campos abaixo e certifique-se que estão corretamente alimentado
- Cód. FPAS
- Taxa Terceiros - INSS
- INSS Terceiros

3. ##### Geração e envio do evento S1020

**Acesse**: Pessoal+  » Rotinas Folha »  Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-1020** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
