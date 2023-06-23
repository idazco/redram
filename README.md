# Red Ram

Red Ram is an acronym which stands for Real Estate Data, Retrieval; Administration; Management.
In other words, this is a tool stack for the retrieval, administration and management of real estate data.
The purpose is to provide a foundation system for building other real estate related solutions.
For example: appraisal, taxation, property management, sales, mortgage origination/management, analytics, marketing, HOA
management and collections.

---

## Considerations

#### Scalability

The stack is put together with scalability in mind. Ultimately however, your own scaling requirements will determine
how you should deploy the stack.

#### Security

- For "local" / one-host deployment:
    - we prefer Podman because it won't run containers as the root user.
    - SSL termination is handled in the reverse proxy with a self-signed cert.

---

## Components

1. Odoo - An extensible ERP which provides the core of the data management. Expand your solution further by creating
   additional Odoo modules in Python.
2. Postgres - The database.
3. Apache Spark - Data ingestion and search are all that's needed for this stack, but of course it provides so much more
   for you to build on.
4. HA Proxy - For reverse proxy and SSL termination.

---

## Requirements

What you require depends on how you want to deploy the stack:

#### One host, "local" deployment

This scenario is typical for a developer or QA person to run the stack on their own machine. You just need to have
Podman installed. Podman can run Docker Compose files, which are provided for launching the complete stack in Podman.
This means you can also run this stack on Mac / Windows.

It is recommended to have a machine with at least 16GB of RAM for running the whole stack on just one host.

#### AWS

Support to be added - Terraform will be used to deploy the stack to AWS.

#### Azure

If there is enough interest, I supposed we can add an Azure deployment via Terraform.

---

## References:

Standards On Mass Appraisal - https://www.iaao.org/media/standards/StandardOnMassAppraisal.pdf



