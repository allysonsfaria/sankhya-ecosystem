---
id: "360057136673"
titulo: "Classificação de Dados"
url: "https://ajuda.sankhya.com.br/hc/pt-br/articles/360057136673-Classifica%C3%A7%C3%A3o-de-Dados"
trilha: "Manual do Produto > Contratos e Serviços > Contratos e Serviços"
atualizado_em: "2026-07-29T14:05:54Z"
rotulos: ["Configuração", "Segurança", "br.com.sankhya.cad.classificacaoLGPD", "Classificação de Dados", "Cadastro", "Classificação de Dados no Sankhya Om", "Anonimização", "Proteção de Dados"]
---

# Classificação de Dados

```
![Módulo](https://ajuda.sankhya.com.br/hc/article_attachments/42311269365911) Módulo: Contratos e Serviços> Arquivos> Cadastros ![Versão](https://ajuda.sankhya.com.br/hc/article_attachments/42311269367319) Versão disponível: A partir da 4.3
```

---

Nesta tela você criará classificações de Dados que serão anonimizados no sistema:

![Imagem 3: Nesta tela você criará classificações de Dados que serão anonimizados no sistema:](https://ajuda.sankhya.com.br/hc/article_attachments/13004337296151)

Depois da criação deste, vincule-o na tela [Grupo de Usuários](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044596134), aba **"Exceções para Proteção de Dados"**. Posteriormente pode-se selecionar esta exceção/classificação no [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294#bot%C3%A3oprote%C3%A7%C3%A3odedados) por meio do botão **"Proteção de Dados"**.

Ainda neste contexto, destacamos que um dado é considerado Pessoal quando ele permite a identificação, sendo esta direta ou indireta da pessoa por pessoa natural por trás do dados, assim teremos por dados Pessoais:

- Nome;
- Sobrenome;
- Data de Nascimento;
- Documentos pessoais (CPF, RG, CNH e Passaporte);
- Endereço residencial ou comercial;
- Telefone;
- E-mail;
- Endereço IP.

Considere por Dados Pessoais Sensíveis:

- Origem racial ou étnica;
- Convicção religiosa;
- Opinião política;
- Filiação a sindicato ou a organização de caráter religioso, filosófico ou político;
- Dado referente à saúde ou à vida sexual;
- Dado genético ou biométrico.

**Observação:** o sistema seguirá uma hierarquia de exceções para campos, sendo que se não houver uma será seguido a anonimização realizada para a próxima e irá ignorar as anteriores, portanto esta hierarquia se dá por: **Exceção de Campo> Exceção de Classificação> Grupo de Usuário> Dicionário de Dados**.

**Nota:** os dados provindos desta tela para o [Dicionário de Dados](https://ajuda.sankhya.com.br/hc/pt-br/articles/360044597294-Dicion%C3%A1rio-de-Dados) só poderão ser excluídos e editados caso você mesmo os tenha inserido.
