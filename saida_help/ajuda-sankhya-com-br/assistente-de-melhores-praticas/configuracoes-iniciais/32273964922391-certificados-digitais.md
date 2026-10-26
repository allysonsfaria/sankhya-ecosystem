---
id: "32273964922391"
titulo: "Certificados Digitais"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/32273964922391-Certificados-Digitais"
trilha: "Assistente de Melhores Práticas > Configurações Iniciais"
atualizado_em: "2026-10-19T16:54:43Z"
rotulos: ["Configuração", "Segurança", "NF-e", "XML", "Documentos Eletrônicos"]
---

# Certificados Digitais

### Descrição

Configuração inicial do **Certificado Digital** para empresas. Garante armazenamento seguro no **Console NF-e** e habilitação para operações fiscais.

Se a matriz e suas filiais compartilharem os primeiros **8 dígitos do CNPJ**, o mesmo certificado digital poderá ser usado para assinar as NF-e de ambas.

O sistema verifica se já existe um certificado cadastrado para essa raiz. Caso exista, não será permitida a inserção de um novo certificado pelo **Assistente de Melhores Práticas**.

**Armazenamento e utilização**

O **Certificado Digital** é armazenado no **Console NF-e**, assegurando sua disponibilidade para os processos fiscais da empresa.

### Como instalar

1. Clique em "**Iniciar**".

2. Selecione o CNPJ raiz para o qual será instalado o Certificado digital.

3. Clique em "**Avançar**".

4. Faça o upload do seu certificado em Modelo A1 com extensão .pfx e digite a senha.

5. Clique em "**Avançar**".

6. Verifique o resumo com as informações dos certificados que serão configurados.

7. Clique em "**Instalar**" para concluir a configuração.

### Detalhes da instalação

Após a instalação, o certificado digital será armazenado no console da NF-e. Se ainda não houver um Certificado cadastrado para o CNPJ raiz escolhido, o novo certificado será marcado como ‘Matriz’, assim todas as filiais podem utilizar o mesmo certificado para a emissão de documentos fiscais.

### Como simular

Para acessar o cadastro realizado:

Acesse a tela **“Console NF-e”**:

1. vá até Comercial > Configuração > Console NF-e;
2. confira os dados inseridos conforme os certificados digitais inseridos.

**Vale saber**

Se a matriz e as filiais compartilham o mesmo CNPJ raiz, basta um único certificado digital para todas. Isso simplifica a gestão e reduz a manutenção. Ao subir o certificado, verifique se ele está no modelo A1 (.pfx) e com a senha correta — isso garante que ele será aceito e armazenado com segurança no Console NF-e.
