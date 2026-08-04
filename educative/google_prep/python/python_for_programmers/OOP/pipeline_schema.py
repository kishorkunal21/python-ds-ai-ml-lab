from pydantic import BaseModel

class PipelineRequest(BaseModel):
    run_id : int
    running : bool
    message : str


pipe = PipelineRequest(run_id=1,running=True,message="123")
print(pipe)
