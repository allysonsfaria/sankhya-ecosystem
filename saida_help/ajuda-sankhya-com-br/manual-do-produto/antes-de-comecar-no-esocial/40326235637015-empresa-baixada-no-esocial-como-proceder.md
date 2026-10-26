---
id: "40326235637015"
titulo: "Empresa Baixada no eSocial: como proceder"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/40326235637015-Empresa-Baixada-no-eSocial-como-proceder"
trilha: "Manual do Produto > Pessoas+ > eSocial > Antes de Começar no eSocial"
atualizado_em: "2026-09-26T00:47:15Z"
rotulos: ["Configuração", "eSocial", "br.com.sankhya.CentraleSocial", "Central do eSocial", "Certificado Digital", "Pessoal+", "Erro", "Empresa Baixada no eSocial", "CNPJ baixado no eSocial", "CNPJ/CPF do Outorgado (Procuração Eletrônica)", "Documentos Eletrônicos"]
---

# Empresa Baixada no eSocial: como proceder

**Módulo:** Pessoal+
**Caminho de acesso:** Pessoal+ > Rotinas Folha > Central do eSocial
**ID da tela:** br.com.sankhya.CentraleSocial

---

### Descrição e Usabilidade

Quando uma empresa possui o CNPJ baixado na Receita Federal, alguns cuidados são necessários para evitar rejeições no eSocial e garantir o envio correto dos eventos pendentes.

Após a baixa do CNPJ na Receita Federal, o eSocial não aceitará novos envios diretamente para esse empregador. E, mesmo com o CNPJ baixado, ainda pode existir necessidade de transmissão de eventos pendentes ao eSocial. Nesse cenário, é comum ocorrer a rejeição abaixo ao enviar eventos na Central do eSocial:

"51 - Número de inscrição baixado no Sistema CNPJ' ao tentar enviar eventos do eSocial. Para a regularização e envio, é necessário outorgar uma Procuração RFB para um CPF ou CNPJ que possua certificado digital válido, conforme FAQ 2.30. O elemento relacionado é /eSocial/evtPgtos/ideEmpregador/nrInsc, valor [10398523].”

Esse retorno indica que:

- o CNPJ utilizado no envio está baixado na Receita Federal;
- ou a procuração/configuração do envio não está sendo considerada corretamente.

### Jornada de Uso

Quando a empresa for efetivamente encerrada:

- finalize os vínculos trabalhistas;
- realize o fechamento das folhas;
- envie os eventos pendentes ao eSocial antes da baixa, sempre que possível;
- transmita desligamentos (S-2299), quando aplicável.

Após a baixa do CNPJ:

- não é necessário encerrar manualmente o S-1000;
- o eSocial bloqueará automaticamente novos envios utilizando o CNPJ baixado;
- poderá ser necessária a utilização de procuração eletrônica vinculada a outro CNPJ ou CPF com certificado digital válido.

#### Procuração e acesso ao eSocial

Em cenários onde o CNPJ original está baixado, o envio dos eventos poderá ocorrer por meio de uma Procuração RFB vinculada a outro CPF ou CNPJ com certificado digital válido.

Para isso:

- informe o **CNPJ/CPF do Outorgado (Procuração Eletrônica)** está preenchido na aba **Informações Fiscais** do [cadastro da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311);
- configure um certificado digital válido na aba **Certificado Digital** do [cadastro da Empresa](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311);
- valide os acessos no eCAC/eSocial;
- confirme se a procuração possui autorização para transmissão dos eventos do eSocial.

⚠️ Caso a TAG do evento continue sendo gerada com o CNPJ baixado, o eSocial continuará retornando a rejeição 51.

### Pontos de Atenção

- Não realize novos envios diretamente com o CNPJ baixado.
- Sempre finalize eventos pendentes antes do encerramento da empresa.
- Revise as configurações de procuração eletrônica antes do envio. Valide o certificado digital utilizado na transmissão. Confirme se o cadastro da empresa possui corretamente:
  - Outorgado da Procuração Eletrônica;
  - certificado digital válido;
  - parametrização fiscal atualizada.
- Caso o erro persista, valide qual CNPJ está sendo montado na TAG do evento enviada ao eSocial.

### Perguntas Frequentes (FAQ)

**1. Preciso encerrar manualmente o S-1000 após a baixa da empresa?**

Não. Após a baixa do CNPJ, o eSocial deixa de aceitar novos envios automaticamente.

**2. O que acontece se eu tentar enviar eventos para um CNPJ baixado?**

O eSocial poderá retornar rejeições informando que a inscrição foi baixada ou não encontrada, como o erro 51.

**3. Posso enviar eventos utilizando procuração eletrônica?**

Sim. É possível utilizar uma Procuração RFB vinculada a outro CPF ou CNPJ com certificado digital válido.

**4. Preciso revisar procuração eletrônica após troca de CNPJ?**

Sim. O novo CNPJ pode exigir nova procuração e novo certificado digital vinculado ao empregador.

**5. Onde informar a procuração eletrônica no sistema?**

No cadastro da Empresa, aba Informações Fiscais, informando o CNPJ/CPF do Outorgado.

**6. O certificado digital da empresa baixada continua funcionando?**

Nem sempre. Após a baixa do CNPJ, o certificado pode perder validade operacional para transmissão ao eSocial.

**7. O que verificar quando a rejeição 51 continuar ocorrendo?**

Verifique:

- procuração eletrônica;
- certificado digital;
- TAG do empregador enviada ao eSocial;
- CNPJ utilizado na transmissão;
- parametrizações fiscais da empresa.

### Artigos Relacionados

- [Cadastro da empresa para a folha de pagamento](https://ajuda.sankhya.com.br/hc/pt-br/articles/37988711948311)
- [Central do eSocial](https://ajuda.sankhya.com.br/hc/pt-br/articles/7064222145175)
