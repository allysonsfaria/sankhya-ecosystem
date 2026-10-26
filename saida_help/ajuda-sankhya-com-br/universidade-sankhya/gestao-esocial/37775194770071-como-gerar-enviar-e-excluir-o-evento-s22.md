---
id: "37775194770071"
titulo: "Como gerar, enviar e excluir o evento S2299"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299"
trilha: "Universidade Sankhya > Gestão eSocial"
atualizado_em: "2026-07-22T14:08:29Z"
rotulos: ["Configuração", "XML", "eSocial", "Folha de Pagamento", "Central do eSocial", "Desligamento"]
---

# Como gerar, enviar e excluir o evento S2299

| Categoria |
| --- |
| [O que é o evento S2299?](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299#h_01KFB5P8FDX7VZG18GA4TQVN2A) |
| [Vídeo com demonstração prática no sistema](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299#h_01KFB5NXFR80WY5TD5WG8F76M8) |
| [Para registrar aviso prévio](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299#h_01KFB5NK60ZKXWP0JGY873BZQW) |
| [Para calcular a recisão](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299#h_01KFB5NB1AXWYMAZ3JY5JCASNM) |
| [Para liberar a folha](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299#h_01KFB5N65GQGFBCCGJ2ZYNTP83) |
| [Para excluir o evento S2299 do portal esocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299#h_01KFB5MYDTHYGBZBQW4SZB7YDZ) |
| [Correção e Repetição](https://ajuda.sankhya.com.br/hc/pt-br/articles/37775194770071-Como-gerar-enviar-e-excluir-o-evento-S2299#h_01KFB5MGR31K90G89FZM1K2XM8) |

## Evento S2299 - Desligamento

#### O que é o evento S2299?

O evento S-2299 é utilizado para registrar no eSocial o desligamento do trabalhador com vínculo empregatício, independentemente do motivo: demissão, término de contrato, aposentadoria, falecimento, entre outros. Ele informa dados como a data de desligamento, motivo, verbas rescisórias e informações de FGTS e INSS, além de permitir a geração correta dos encargos relacionados à rescisão. Esse evento deve ser enviado até 10 dias após o desligamento, e é fundamental para encerrar corretamente o vínculo no sistema, evitando pendências na DCTFWeb ou no FGTS Digital.

##### Vídeo com demonstração prática no sistema

[Vídeo: tutorial do artigo](https://player.vimeo.com/video/1106240528)

####

#### É o momento de aplicar o conhecimento adquirido! Realize as movimentações no ERP Sankhya

1. ##### Para registrar aviso prévio

**Acesse**: Pessoal+ » Cadastros » Aviso Prévio

- Preencha todas as informações solicitadas na tela e salve o registro

2. ##### Para calcular a recisão

**Acesse**:  Pessoal+  » Rotinas Folha » Cálculos

- Selecione o tipo de cálculo e a folha
- Em Informações Gerais preencha "Referência", "Data de Pagamento", "Empresa", "Funcionário" e "Data de Demissão"
- Preencha as informações referente ao Tipo de Rescisão e FGTS
- Preencha a etapa de Desligamento apenas nos casos de decisão judicial, falecimento do trabalhador ou exoneração de diretores.
- Informe os dados referentes ao aviso prévio
- Defina o modo de cálculo e acione o botão “Calcular”

3. ##### Para liberar a folha

**Acesse**: Pessoal+ » Rotinas Folha » Gerenciador de Folhas

- Na lateral direita da tela, clique no botão Liberação para eSocial
- Informe a referência do cálculo
- Defina o tipo de ação “Liberar dados”
- Selecione a empresa no resultado dos filtros
- Na aba Funcionários selecione os funcionários que terão os dados da folha bloqueados para o esocial
- Clique no botão “Liberar dados para eSocial”

4. **Geração e envio do evento S2299**

**Acesse**: Pessoal+  » Rotinas Folha » Central do eSocial

- Na lateral esquerda da tela, selecione a empresa, a referência e o ambiente de envio, e em seguida clique em '**Carregar**'.
- No menu lateral, acesse a aba “**Geração**” e escolha a opção **Individual**
- Selecione o evento **S-2299** e em seguida clique em “**Iniciar** **Geração**”
- Após a geração, o evento será listado como card na aba '**Eventos Pendentes**'. Para realizar a transmissão ao eSocial, utilize o botão '**Enviar dados**'

Após o envio, o evento ficará na aba '**Eventos na Fila**' até a conclusão do processamento pelo ambiente do eSocial. Finalizado o envio, ele será movido para a aba '**Acompanhamento**', onde é possível visualizar os dados enviados e os XMLs de retorno por meio do botão '**Visualizar dados**'

5. ##### Para excluir o evento S2299 do portal esocial

**Acesse**: Pessoal+ » Rotinas Folha » Gerenciador de Folhas

- Na lateral direita da tela, clique no botão Liberação para eSocial
- Informe a referência do cálculo
- Defina o tipo de ação “Bloquear dados”
- Selecione a empresa no resultado dos filtros
- Na aba Funcionários selecione os funcionários que terão os dados da folha bloqueados para o esocial
- Clique no botão “Bloquear liberação”
- Retorne à Central do eSocial e gere novamente o evento S2299 para enviar a exclusão.

#### Correção e Repetição

- Revise os registros para confirmar se os passos foram seguidos.
- Caso haja erro no registro verifique atentamente os campos mencionados no erro e consulte o manual do eSocial.
