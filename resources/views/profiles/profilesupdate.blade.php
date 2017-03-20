@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="row">
            <div class="col-md-8 col-md-offset-2">
                <div class="panel panel-default">
                    <div class="panel-heading">Dashboard</div>

                    <div class="panel-body">
                        <div class="row col-md-6">
                            <form method="POST" action="{{ route('profileStore')}}">
                                {{ csrf_field() }}
                                <div class="form-group">
                                    <label for="weixin">微信号</label>
                                    <input type="text" class="form-control" name="weixin" value="{{$weixin}}">
                                </div>

                                <button type="submit" class="btn btn-success">修改</button>
                            </form>
                        </div>

                    </div>

                </div>
            </div>

        </div>

    </div>
    </div>
@endsection
