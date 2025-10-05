from typing import Any

from infrahub_sdk.generator import InfrahubGenerator


class DeploymentGenerator(InfrahubGenerator):
    async def generate(self, data: dict[str, Any]) -> None:
        change_id = data["CoreProposedChange"]["edges"][0]["node"]["id"]
        change = await self.client.get(kind="CoreProposedChange", ids=[change_id])

        if change.state.value == "merged":
            deployment_obj = await self.client.create(
                kind="ChangeDeployment",
                name=f"deployment-{change_id}",
                status="requested",
                proposed_change=change,
            )
            await deployment_obj.save(upsert=True)
