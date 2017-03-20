@extends('layouts.app')

@section('content')
<div class="container">
    <div class="row">
        <div class="col-md-8 col-md-offset-2">
            <div class="panel panel-default">
                <div class="panel-heading">Dashboard</div>

                <div class="panel-body">
                    <table class="table table-striped">
                        <tr>
                            <th>项目</th>
                            <th>内容</th>
                        </tr>
                        <tr>
                            <td>微信号</td>
                            <td>{{ $weixin }}</td>
                        </tr>
                    </table>
                    <row>
                        <a href="{{ route('profilesUpdate') }}" class="btn btn-success">修改</a>
                    </row>
                </div>

                </div>
            </div>

        </div>

    </div>
</div>
@endsection
