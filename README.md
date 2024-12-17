
# Case de Engenharia de Dados

Este repositório contém um case voltado para operações de dados. O objetivo principal não é demonstrar o uso de ferramentas específicas, mas sim enfatizar a tomada de decisões estratégicas e a disseminação de boas práticas aplicáveis a uma audiência ampla.

A parte técnica utiliza tecnologias amplamente conhecidas e acessíveis, com grande suporte em fóruns e ferramentas como IA. Na Visio, acreditamos que a capacidade de pesquisa e aprendizado contínuo é muito mais valiosa do que o domínio exclusivo de uma ferramenta. Valorizamos profissionais curiosos, que se interessam por explorar novas tecnologias e encontrar soluções inovadoras.

Este case é inspirado em um cenário realista, que reflete desafios iniciais típicos enfrentados por engenheiros de dados. Algumas complexidades foram simplificadas para alinhar o case às demandas e restrições de tempo comuns no final do ano, permitindo um foco mais prático e direto.


## Considerações importantes
- O Postgres será utilizado como banco OLAP para este exercício.
- Em cenários reais, paga-se tanto pelo armazenamento quanto pela recuperação de dados em queries.
- O custo das queries geralmente é significativamente mais alto que o de armazenamento, tornando essencial a otimização das consultas para minimizar custos.
- Os times de negócio consultam os dados via dashboards várias vezes ao dia, resultando em uma alta frequência de execução de queries.
- Apesar de técnicas como particionamento e clusterização serem úteis, o foco deste case está na organização de tabelas para consultas eficientes e inteligentes.
- Documentação clara é fundamental: múltiplas equipes trabalham em diferentes contextos simultaneamente, tornando playbooks e documentação escrita essenciais para alinhar soluções.

## Carregando os dados raw
Nesta etapa, faremos a extração dos dados. Para simplificar, os dados foram disponibilizados em formato JSON, eliminando a necessidade de interação com APIs. Eles representam cupons fiscais de uma loja fictícia.

Os dados de cupons fiscais são a base da maioria das análises realizadas para diversos clientes. Geralmente, esses dados estão em bancos não relacionais, mas, neste case, estão em arquivos para facilitar a manipulação. Cada arquivo contém uma lista de cupons vendidos em um dia. Abaixo, segue a descrição dos campos:

```json
{
    "coupon": "1AM5250082", //ID do cupom, é único nesse caso em particular
    "date_time": "20/12/2023 06:45:00", // Datetime do horário local de estração
    "price_total": "40.00", // O preço total do cupom fiscal
    "payments": [ // aqui é uma lista pq pode haver múltiplos meios de pagamento
    {
        "type": "Dinheiro", //Tipo do pagmento
        "amount": "40.00" // valor pago
    }
    ],
    "timestamp_erp": 1703054700, //timestamp do cupom
    "details": { //esses detalhes podem ser ignorados para essa atividade, mas eles representa informações sobre o computador que emitiu a nota fiscal
        "movimento": "",
        "operator": "00256",
        "abertura": "",
        "pdv": "14"
    },
    "fee": "4.29", //Taxas pagas no geral
    "delivery": false, //Se o cupom é delivery
    "staff": false, // Se o cupom é dos funcionários
    "items": [ // lista do itens presentes na loja
        {
            "item": "Sanduíche Bauru", // nome do item
            "canceled": "false", //Se foi cancelado
            "total": "20.00", // Valor total dos itens desse tipo
            "price": "20.00", // Preço individual do item
            "quantity": 1 // Quantidade comprada
        }
    ]
}
```
### Requisitos para Carregamento
- Os dados brutos devem ser carregados no Postgres.
- Escolha a ferramenta ou método que preferir (ex.: scripts em Python ou aplicações).
- Regras:
    - Cupons iniciados com 4 indicam delivery.
    - Cupons iniciados com 3 indicam autoatendimento.
    - Cupons iniciados com 1 indicam consumo no restaurante.

```
⚠️ O ambiente já está configurado com Docker Compose para subir o Spark e o banco de dados Postgres, garantindo a replicabilidade do projeto.
```

## Transformando os dados do banco
Nesta etapa, utilizaremos o Spark para transformar os dados. Embora o volume de dados seja pequeno, o objetivo é simular um cenário de grande escala, onde fluxos contínuos de dados precisam ser processados.

O foco aqui é demonstrar a utilização de uma ferramenta robusta e popular de pipelines de dados.


### Checando se o spark está funcionado
Após subir o compose, entre dentro do container executando o comando a seguir:
```bash
sudo docker compose exec -it spark bash
```

Dentro do container, é possível executar o exemplo que deixei pronto, com o seguinte comando:
```bash
spark-submit  /opt/spark-apps/example.py
```

## Perguntas que o time de negócio geralmente quer responder

Nosso objetivo é auxiliar o time de negócios a obter insights significativos. As perguntas mais comuns incluem:

- Qual é o faturamento da loja em diferentes períodos de tempo (diário, semanal e mensal)?
- Quais são os itens mais vendidos e menos vendidos? Quais itens geram mais faturamento?
- Quais são os métodos de pagamento mais utilizados?
- Quais são os horários de maior movimento?
- Qual é a divisão de vendas por modalidade (delivery, restaurante e autoatendimento)?

💡 Nota: É importante garantir que essas perguntas possam ser respondidas com consultas eficientes e que minimizem a quantidade de dados processados.



### Visualizando os dados
Use a ferramenta de visualização de sua preferência (ex.: Tableau, Metabase, Grafana). Adicione-a ao docker-compose.yml para que possa ser executada localmente e visualizar os dashboards.

⚠️ Observação: O formato dos gráficos não é o foco; o importante é verificar o funcionamento das queries com seletores de datas.

 ## Submissão e o que será avaliado
- Caso o repositório esteja privado, adicione-me como colaborador para que eu possa clonar o projeto.
- A avaliação seguirá a documentação fornecida para replicar o ambiente e verificar os resultados.

 ### Principais pontos de avaliação
1. Qualidade da documentação, especialmente para desenvolvedores.
2. Organização e transformação dos dados no pipeline.
3. Estrutura e organização das tabelas geradas.
4. Explicação clara das escolhas realizadas.
5. Documentação voltada ao time de negócios para utilização das tabelas.
