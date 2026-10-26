---
id: "360048501274"
titulo: "Como gerar os registros C195 e C197 da EFD- Escrituração Fiscal Digital"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360048501274-Como-gerar-os-registros-C195-e-C197-da-EFD-Escritura%C3%A7%C3%A3o-Fiscal-Digital"
trilha: "Dúvidas Frequentes > Fiscal e Contábil"
atualizado_em: "2026-07-22T15:31:29Z"
rotulos: ["Configuração", "Fiscal", "SEFAZ", "EFD", "avulsa", "Configurar tipo de escrituração", "Gerar registros 0460", "Registros C195 e C197 EFD", "Documentos Eletrônicos"]
---

# Como gerar os registros C195 e C197 da EFD- Escrituração Fiscal Digital

![Imagem 1: Acesse a tela Empresa (Comercial » Preferências » Empresa) Aba Escrituração Fiscal Digital >> Tipo de escrituração…](https://ajuda.sankhya.com.br/hc/article_attachments/18940577294743)Acesse a tela **Empresa** (Comercial » Preferências » Empresa) Aba Escrituração Fiscal Digital >> Tipo de escrituração 'EFD':

- Verifique no Bloco C, se os Registros C195/C197 estão marcados para gerar:

![Imagem 2: Verifique no Bloco C, se os Registros C195/C197 estão marcados para gerar:](https://ajuda.sankhya.com.br/hc/article_attachments/18940577303191)

Marque também para gerar os registros 0460:

![Imagem 3: Marque também para gerar os registros 0460:](https://ajuda.sankhya.com.br/hc/article_attachments/18940577310615)

![Imagem 4: Acesse a rotina 'Observações para Notas' (Comercial » Arquivo » Cadastros » Observações para Notas) e cadastrar uma…](https://ajuda.sankhya.com.br/hc/article_attachments/18940584145815) Acesse a rotina **'Observações para Notas'** (Comercial » Arquivo » Cadastros » Observações para Notas)e cadastrar uma observação padrão com as seguintes configurações:

- Geração no EFD: Observação do Lançamento Fiscal
- Carrega complemento para EFD: Marcado
- Para mais detalhes: [Observações para Notas](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596474)

Defina uma das opções abaixo para geração dos respectivos registros:

![Imagem 5: Caso seja necessário gerar esses registros para um volume muito grande de nota recomendamos configurar o ajuste…](https://ajuda.sankhya.com.br/hc/article_attachments/18940584148503) Caso seja necessário gerar esses registros para um volume muito grande de nota recomendamos configurar o **ajuste automático**, através da rotina 'Configurações de Ajustes de Apuração' (Livros Fiscais » Arquivos » Configurações de Ajustes de Apuração).

Nesta tela, o campo **'Tipo de Configuração'** deverá estar configurado com o tipo **'1 - Ajustes de Documento'** e os dados para ajuste informados na **aba 'Ajustes de Documentos - EFD Fiscal'.** As informações inseridas nessa aba irão popular a aba 'Ajustes de Documentos - EFD Fiscal' (Tela: Cadastro Livro ICMS/IPI )

- Para mais detalhes:  [Configurações de Ajustes de Apuração](https://ajuda.sankhya.com.br/hc/pt-br/articles/360045110593)

![Imagem 6: Caso não deseje configurar o ajuste automático, manualmente será possível selecionar o documento(nota) que deseja gerar…](https://ajuda.sankhya.com.br/hc/article_attachments/18940577331351) Caso não deseje configurar o ajuste automático, **manualmente** será possível selecionar o documento(nota) que deseja gerar o C195/C197 e na aba correspondente:  Ajustes de Documentos - EFD Fiscal' inserir as informações necessárias para que o registro seja gerado no SPED ICMS/IPI conforme exemplo abaixo:

**Cód.Obs.Padrão**: Cadastro conforme item 2.

**Cód.Ajuste:** Informar o código de Ajuste de acordo com a UF da empresa emitente da nota, este código é conseguido no seguinte site: <http://sped.rfb.gov.br/pagina/show/1578>

- Escolha a opção: EFD ICMS/IPI>> Downloads e baixar a tabela conforme a UF da empresa emitente.
- Escolha o código dentro do arquivo txt de códigos que será baixado

![Imagem 7: Escolha o código dentro do arquivo txt de códigos que será baixado](https://ajuda.sankhya.com.br/hc/article_attachments/18940584164375)

- Informe o valor do Ajuste em um dos campos, conforme necessidade:

![Imagem 8: Informe o valor do Ajuste em um dos campos, conforme necessidade:](https://ajuda.sankhya.com.br/hc/article_attachments/18940584169111)

![Imagem 9: Por fim, gere o arquivo EFD e verificar se os registros foram gerados com sucesso:](https://ajuda.sankhya.com.br/hc/article_attachments/18940577352471) Por fim, gere o arquivo EFD e verificar se os registros foram gerados com sucesso:

![Imagem 10: Por fim, gere o arquivo EFD e verificar se os registros foram gerados com sucesso:](https://ajuda.sankhya.com.br/hc/article_attachments/360073257893)
