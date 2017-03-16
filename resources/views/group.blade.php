@extends('layouts.app')

@section('content')
    <div class="container">
        <div class="row">
            <table class="table table-striped">
                <tr>
                    <th>名称</th>
                    <th>说明</th>
                    <th>网址</th>
                    <th>参加</th>
                </tr>
                @foreach($items as $item)
                    <tr>
                        <td>{{$item->name}}</td>
                        <td>{{str_limit($item->detail, $limit = 100, $end = '...') }}</td>
                        <td>{{$item->url}}</td>
                        <td><button>参与</button></td>
                    </tr>
                @endforeach
            </table>
        </div>
        {{ $items->links() }}
    </div>
@endsection
