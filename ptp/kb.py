import muscadet

class Start(muscadet.ObjFlow):

    def add_flows(self, **kwargs):

        super().add_flows(**kwargs)

        self.add_flow_out(
            name="flow",
        )

class Task(muscadet.ObjFlow):

    def add_flows(self, duration_min=0, duration_max=0, **kwargs):

        super().add_flows(**kwargs)

        self.add_flow_in(
            name="flow",
        )

        self.add_flow_out_tempo(
            name="flow",
            var_prod_cond=[
                "flow",
            ],
            flow_init_state="stop",
            occ_start_flow=dict(cls="uniform", min=duration_min, max=duration_max),
        )


class End(muscadet.ObjFlow):

    def add_flows(self, **kwargs):

        super().add_flows(**kwargs)

        self.add_flow_in(
            name="flow",
        )
